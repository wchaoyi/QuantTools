from QUANTTOOLS.QAStockTradingDay.StockStrategySecond.trading import trading
from QUANTAXIS.QAUtil import QA_util_today_str,QA_util_get_last_day,QA_util_get_real_date


if __name__ == '__main__':
    if QA_util_get_last_day(QA_util_today_str()) == 'wrong date':
        mark_day = QA_util_get_real_date(QA_util_today_str())
    else:
        mark_day = QA_util_get_last_day(QA_util_today_str())
    trading(mark_day)