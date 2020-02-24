from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_list
from QUANTAXIS.QAFetch import QA_fetch_get_stock_realtime
from QUANTTOOLS.message_func.wechat import send_actionnotice
from QUANTTOOLS.QAStockTradingDay.StrategyOne import load_model, model_predict
from QUANTTOOLS.QAStockETL.QAFetch import QA_fetch_stock_fianacial_adv
import pandas as pd
import logging
import strategyease_sdk
from QUANTTOOLS.message_func import send_email
from QUANTTOOLS.QAStockTradingDay.setting import working_dir, yun_ip, yun_port, easytrade_password
from QUANTAXIS.QAUtil import QA_util_log_info
import time
import datetime
from QUANTTOOLS.account_manage.trading_message import send_trading_message

def build(tar, positions, sub_accounts, trading_date):
    r1 = pd.concat([tar,
                    positions.set_index('证券代码')],axis=1)
    r1['可用余额'] = r1['可用余额'].fillna(0)
    realtm = QA_fetch_get_stock_realtime('tdx', code=[x for x in list(r1.index) if x in list(QA_fetch_stock_list().index)]).reset_index('datetime')[['ask1','ask_vol1','bid1','bid_vol1']]
    res = pd.concat([r1,
                     realtm,
                     QA_fetch_stock_fianacial_adv(list(r1.index), trading_date, trading_date).data.reset_index('date')[['NAME','INDUSTRY']]],
                    axis=1)
    avg_account = sub_accounts['总 资 产']/tar.shape[0]
    res = res.assign(tar=avg_account[0])
    res.ix[res['RANK'].isnull(),'tar'] = 0
    res['cnt'] = (res['tar']/res['ask1']/100).apply(lambda x: round(x, 0)*100)
    res['real'] = res['cnt'] * res['ask1']
    res = res.sort_values(by='ask1', ascending= False)
    res = res.fillna(0)
    res1 = res[res['tar']>0]
    res2 = res[res['tar']==0]
    res1.ix[-1, 'cnt'] = round((res1['real'][-1]-(res1['real'].sum()-res1['tar'].sum()))/res1['ask1'][-1]/100,0)*100-100
    res = pd.concat([res1,res2])
    res['real'] = res['cnt'] * res['ask1']
    res['mark'] = res['cnt'] - res['可用余额'].apply(lambda x:float(x))
    return(res)

def trade_roboot(tar, account, trading_date, strategy_id):
    logging.basicConfig(level=logging.DEBUG)
    client = strategyease_sdk.Client(host=yun_ip, port=yun_port, key=easytrade_password)
    account1=account
    client.cancel_all(account1)
    account_info = client.get_account(account1)
    sub_accounts = client.get_positions(account1)['sub_accounts']
    positions = client.get_positions(account1)['positions'][['证券代码','证券名称','股票余额','可用余额','冻结数量','参考盈亏','盈亏比例(%)']]

    res = build(tar, positions, sub_accounts, trading_date)
    res1 = res
    while res[res['mark']<0].shape[0] + res[res['mark']>0].shape[0] > 0:

        if res[res['mark']<0].shape[0] == 0:
            pass
        else:
            for i in res[res['mark'] < 0].index:
                cnt = float(res.at[i, 'cnt'])
                tar = float(res.at[i, 'real'])
                NAME = res.at[i, 'NAME']
                INDUSTRY = res.at[i, 'INDUSTRY']
                mark = abs(float(res.at[i, 'mark']))

                print('卖出 {code}({NAME},{INDUSTRY}) {cnt}股, 目标持仓:{target},总金额:{tar}'.format(code=i,
                                                                                            NAME= NAME,
                                                                                            INDUSTRY= INDUSTRY,
                                                                                            cnt=abs(mark),
                                                                                            target=cnt,
                                                                                            tar=tar))
                e = send_trading_message(account1, strategy_id, account_info, i, NAME, INDUSTRY, mark, direction = 'SELL', type='MARKET', priceType=4, client=client)
                time.sleep(5)
        time.sleep(30)

        for i in res[res['mark'] == 0].index:
            cnt = float(res.at[i, 'cnt'])
            tar = float(res.at[i, 'real'])
            NAME = res.at[i, 'NAME']
            INDUSTRY = res.at[i, 'INDUSTRY']
            mark = abs(float(res.at[i, 'mark']))
            print('继续持有 {code}({NAME},{INDUSTRY}), 目标持仓:{target},总金额:{tar}'.format(code=i,
                                                                                   NAME= NAME,
                                                                                   INDUSTRY=INDUSTRY,
                                                                                   target=cnt,
                                                                                   tar=tar))
            send_actionnotice(strategy_id,
                              account_info,
                              '{code}({NAME},{INDUSTRY})'.format(code=i,NAME= NAME, INDUSTRY=INDUSTRY),
                              direction = 'HOLD',
                              offset='HOLD',
                              volume=abs(mark)
                              )

        time.sleep(10)
        if res[res['mark'] > 0].shape[0] == 0:
            pass
        else:
            for i in res[res['mark'] > 0].index:
                cnt = float(res.at[i, 'cnt'])
                tar = float(res.at[i, 'real'])
                NAME = res.at[i, 'NAME']
                INDUSTRY = res.at[i, 'INDUSTRY']
                mark = abs(float(res.at[i, 'mark']))
                print('买入 {code}({NAME},{INDUSTRY}) {cnt}股, 目标持仓:{target},总金额:{tar}'.format(code=i,
                                                                                            NAME= NAME,
                                                                                            INDUSTRY=INDUSTRY,
                                                                                            cnt=abs(mark),
                                                                                            target=cnt,
                                                                                            tar=tar))
                e = send_trading_message(account1, strategy_id, account_info, i, NAME, INDUSTRY, mark, direction = 'BUY', type='MARKET', priceType=4, client=client)
                time.sleep(5)
        res = build(tar, positions, sub_accounts, trading_date)

    return(res1)