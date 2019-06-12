import pandas as pd
from QUANTTOOLS.QAStockETL.QAFetch.QAQuery_Advance import (QA_fetch_stock_fianacial_adv,QA_fetch_stock_alpha_adv,QA_fetch_stock_technical_index_adv)
from QUANTAXIS.QAFetch.QAQuery_Advance import (QA_fetch_stock_list_adv, QA_fetch_stock_block_adv,
                                               QA_fetch_stock_day_adv)
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_basic_info_tushare
from  QUANTAXIS.QAUtil import (QA_util_date_stamp,QA_util_today_str,
                               QA_util_if_trade,QA_util_get_pre_trade_date)
import QUANTAXIS as QA

def perank(data):
    data['PE_5PCT']= data['PE'].rolling(window=5).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_10PCT']= data['PE'].rolling(window=10).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x, 2)),raw=True)
    data['PE_20PCT']= data['PE'].rolling(window=20).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_30PCT']= data['PE'].rolling(window=30).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_60PCT']= data['PE'].rolling(window=60).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_5VAL']= data['PE'].rolling(window=5).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_10VAL']= data['PE'].rolling(window=10).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_20VAL']= data['PE'].rolling(window=20).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_30VAL']= data['PE'].rolling(window=30).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PE_60VAL']= data['PE'].rolling(window=60).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_5PCT']= data['PB'].rolling(window=5).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_10PCT']= data['PB'].rolling(window=10).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x, 2)),raw=True)
    data['PB_20PCT']= data['PB'].rolling(window=20).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x, 2)),raw=True)
    data['PB_30PCT']= data['PB'].rolling(window=30).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_60PCT']= data['PB'].rolling(window=60).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_5VAL']= data['PB'].rolling(window=5).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_10VAL']= data['PB'].rolling(window=10).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_20VAL']= data['PB'].rolling(window=20).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_30VAL']= data['PB'].rolling(window=30).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PB_60VAL']= data['PB'].rolling(window=60).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_5PCT']= data['PEG'].rolling(window=5).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_10PCT']= data['PEG'].rolling(window=10).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x, 2)),raw=True)
    data['PEG_20PCT']= data['PEG'].rolling(window=20).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x, 2)),raw=True)
    data['PEG_30PCT']= data['PEG'].rolling(window=30).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_60PCT']= data['PEG'].rolling(window=60).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_5VAL']= data['PEG'].rolling(window=5).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_10VAL']= data['PEG'].rolling(window=10).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_20VAL']= data['PEG'].rolling(window=20).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_30VAL']= data['PEG'].rolling(window=30).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PEG_60VAL']= data['PEG'].rolling(window=60).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_5PCT']= data['PS'].rolling(window=5).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_10PCT']= data['PS'].rolling(window=10).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x, 2)),raw=True)
    data['PS_20PCT']= data['PS'].rolling(window=20).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x, 2)),raw=True)
    data['PS_30PCT']= data['PS'].rolling(window=30).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_60PCT']= data['PS'].rolling(window=60).apply(lambda x: pd.DataFrame(x).rank(pct=True).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_5VAL']= data['PS'].rolling(window=5).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_10VAL']= data['PS'].rolling(window=10).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_20VAL']= data['PS'].rolling(window=20).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_30VAL']= data['PS'].rolling(window=30).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    data['PS_60VAL']= data['PS'].rolling(window=60).apply(lambda x: (pd.DataFrame(x)-pd.DataFrame(x).median()).iloc[-1].apply(lambda x:round(x , 2)),raw=True)
    return(data)

def QA_fetch_get_stock_financial_percent(code,start_date,end_date):
    start = QA_util_get_pre_trade_date(start_date,61)
    fianacial = QA_fetch_stock_fianacial_adv(code,start,end_date).data[['PB', 'PE', 'PEG', 'PS']].groupby('code').fillna(method='ffill')
    fianacial = fianacial.groupby('code').apply(perank).loc[pd.Series(pd.date_range(start_date, end_date, freq='D')).apply(lambda x: str(x)[0:10])].reset_index()
    fianacial = fianacial.assign(date_stamp=fianacial['date'].apply(lambda x: QA_util_date_stamp(str(x)[0:10])))[[x for x in list(fianacial.columns) if x not in ['PB', 'PE', 'PEG', 'PS']]]
    return(fianacial)