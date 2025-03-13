import random
import time

def simulate_trade():
    price = random.uniform(100, 200)  # Simulate crypto price
    action = random.choice(["BUY", "SELL", "HOLD"])
    print(f"Simulated Price: ${price:.2f} | Action: {action}")
    return {"price": price, "action": action}

if __name__ == "__main__":
    print("Starting Hello-Trading Simulation...")
    for _ in range(5):
        result = simulate_trade()
        time.sleep(1)  # Simulate latency
    print("Simulation Complete!")