
# Trading Agent Simulation

A simple trading simulation project that models a trading agent making buy/sell decisions based on random market sentiment, built with Python and containerized using Docker.

## Project Structure

```
trading-agent/
├── src/                # Core simulation code
│   ├── __init__.py
│   ├── trader.py      # Trader class with sentiment logic
│   └── simulation.py  # Main simulation runner
├── tests/             # Unit tests
│   ├── __init__.py
│   └── test_trader.py
├── .github/           # CI/CD configuration
│   └── workflows/
│       └── ci.yml
├── Dockerfile         # Docker configuration
├── README.md          # This file
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
└── .dockerignore      # Docker ignore rules
```

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed.
- [Git](https://git-scm.com/) installed (optional, for cloning).
- Python 3.9+ (optional, for local runs without Docker).

## Setup and Running

### Using Docker

1. **Clone the Repository** (if not already local):
   ```bash
   git clone https://github.com/rakshitha2207/Automated-Trading-Agent.git
   cd trading-agent
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t rakshitha919/trading-agent .
   ```
   - Builds the image using the `Dockerfile` and tags it as `rakshitha919/trading-agent`.

3. **Run the Simulation**:
   ```bash
   docker run rakshitha919/trading-agent
   ```
   - Executes the trading simulation, showing daily actions and final portfolio value.

### Running Locally (Optional)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the simulation:
   ```bash
   python src/simulation.py
   ```

## Testing

- **Locally**:
  ```bash
  pytest tests/
  ```
- **Via CI/CD**: Tests run automatically on push/pull requests via GitHub Actions. Check the "Actions" tab in the repository.

## CI/CD

- A GitHub Actions workflow (`.github/workflows/ci.yml`) runs unit tests on every push or pull request to the `main` branch.
- To verify:
  1. Push changes to your GitHub repo.
  2. Visit `https://github.com/rakshitha2207/Automated-Trading-Agent/actions` to see the pipeline status.




   
