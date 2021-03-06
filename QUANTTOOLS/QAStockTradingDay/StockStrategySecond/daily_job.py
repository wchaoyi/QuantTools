from datetime import datetime
from QUANTTOOLS.QAStockTradingDay.StockStrategySecond.train import train
from QUANTTOOLS.QAStockTradingDay.StockStrategySecond.running import predict
from QUANTTOOLS.QAStockTradingDay.StockStrategySecond.setting import working_dir
from QUANTAXIS.QAUtil.QADate_trade import QA_util_if_trade,QA_util_get_real_date,QA_util_get_last_day

def job111(trading_date):

    if datetime.strptime(trading_date, "%Y-%m-%d").weekday() == 4:
        if QA_util_if_trade(trading_date):
            pass
        else:
            trading_date = QA_util_get_last_day(trading_date, 1)

        predict(QA_util_get_last_day(trading_date))
        train(trading_date, working_dir=working_dir)
    else:
        pass

    if QA_util_if_trade(trading_date):
        predict(trading_date)
    else:
        predict(QA_util_get_real_date(trading_date))


