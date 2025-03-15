from src.trader import Trader

def test_trader_init():
    trader = Trader(initial_cash=500)
    assert trader.cash == 500
    assert trader.shares == 0
    assert trader.stock_price == 100

def test_sentiment_range():
    trader = Trader()
    sentiment = trader.get_sentiment()
    assert -1 <= sentiment <= 1