# Selenium Parallel Execution Framework ⚡

An elite, highly scalable automation boilerplate utilizing **Python, Selenium WebDriver, Pytest, and Docker** designed for industrial-strength UI automation.

## 🚀 Key Architectural Pillars

### 1. High-Performance Infrastructure
- **Dependency Management**: Powered by `Poetry` for deterministic, lock-file based environments.
- **BaaS Abstraction**: A "Browser-as-a-Service" layer to seamlessly toggle between local containers and a scaled Selenium Grid.
- **Hub/Node Scaling**: Refactored `docker-compose` for horizontal scaling of Chrome and Firefox nodes.

### 2. Radical Reliability & Type Safety
- **BasePage Architecture**: Robust explicit waits and common interaction patterns encapsulated in a central base class.
- **Strict Protocols**: Protocol-based interaction contracts ensuring type safety across the framework.
- **Atomic Page Objects**: Designed to move from monolithic pages to reusable UI components.

### 3. Deep Observability & DevEx
- **Rich Reporting**: Automated Allure reports with integrated failure screenshots and browser log capture.
- **Sandbox CLI**: A dedicated `sandbox.py` script for rapid environment setup and test execution.
- **Data Isolation**: API-First Data Factory patterns for instant, isolated test state initialization.

## 🛠 Project Layout

```text
.
├── src/framework/       # Core framework library
│   ├── components/      # Atomic UI components & BasePage
│   ├── core/            # Config, Factory, and Protocols
│   ├── data/            # API-driven Data Factorites
│   └── observability/   # Tracing, Logging, and Reporting
├── tests/               # Test suites (web, api, mobile)
├── scripts/             # Developer utilities (sandbox.py)
├── pyproject.toml       # Poetry configuration
└── docker-compose.yml   # Scalable Selenium Grid
```

## 🏁 Getting Started

### 1. Prerequisites
- Python 3.10+
- Docker & Docker Compose
- [Poetry](https://python-poetry.org/docs/#installation)

### 2. Setup
```bash
poetry install
```

### 3. Execution via Sandbox
```bash
# Start the Selenium Grid
python3 scripts/sandbox.py up

# Run tests in parallel (4 workers) against local grid
python3 scripts/sandbox.py test --workers 4 --env grid

# Stop the grid
python3 scripts/sandbox.py down
```

## 📊 Reporting
After running tests, generate the Allure report:
```bash
python3 scripts/sandbox.py report
```
