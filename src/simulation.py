from trader import Trader

def run_simulation(days=10):
    trader = Trader()
    print(f"Starting cash: ${trader.cash}, Shares: {trader.shares}")
    for day in range(1, days + 1):
        trader.update_price()
        action = trader.decide()
        print(f"Day {day}: Price ${trader.stock_price:.2f}, {action}, Cash: ${trader.cash:.2f}, Shares: {trader.shares}")
    total_value = trader.cash + trader.shares * trader.stock_price
    print(f"Final value: ${total_value:.2f}")

if __name__ == "__main__":
    run_simulation()