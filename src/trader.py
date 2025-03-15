import random

class Trader:
    def __init__(self, initial_cash=1000):
        self.cash = initial_cash
        self.shares = 0
        self.stock_price = 100  # Starting price

    def get_sentiment(self):
        """Simulate market sentiment (random score between -1 and 1)."""
        return random.uniform(-1, 1)

    def decide(self):
        """Make a buy/sell decision based on sentiment."""
        sentiment = self.get_sentiment()
        if sentiment > 0.5 and self.cash >= self.stock_price:
            # Buy if sentiment is strongly positive
            shares_to_buy = self.cash // self.stock_price
            self.cash -= shares_to_buy * self.stock_price
            self.shares += shares_to_buy
            return f"Bought {shares_to_buy} shares at ${self.stock_price}"
        elif sentiment < -0.5 and self.shares > 0:
            # Sell if sentiment is strongly negative
            cash_earned = self.shares * self.stock_price
            self.cash += cash_earned
            shares_sold = self.shares
            self.shares = 0
            return f"Sold {shares_sold} shares at ${self.stock_price}"
        return "No action"

    def update_price(self):
        """Randomly update stock price."""
        self.stock_price *= random.uniform(0.95, 1.05)  # 5% fluctuation