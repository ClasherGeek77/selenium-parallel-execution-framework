# selenium-paralel ⚡

[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-success?logo=selenium)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Framework-Pytest-blue?logo=pytest)](https://docs.pytest.org/en/7.4.x/)
[![Docker](https://img.shields.io/badge/Infrastructure-Docker-blue?logo=docker)]()

An advanced, highly scalable automation framework utilizing **Python, Selenium WebDriver, Pytest**, and **Docker** to execute tests in parallel across multiple nodes.

## 🎯 Objective
To dramatically reduce test suite execution times and showcase modern SDET infrastructure architecture by executing UI tests concurrently via `pytest-xdist` against a containerized Selenium Grid.

## 🏗 Architecture & Technologies
- **Language**: Python 3
- **Test Runner**: Pytest (with `pytest-xdist` for parallelization)
- **UI Interaction**: Selenium WebDriver
- **Infrastructure**: Docker & Docker Compose (Browser Nodes)

## ⚙️ Key Technical Highlights
1. **Parallel Execution Engine**: Tests are distributed across CPU cores or nodes, slashing build times by up to 80% compared to serial execution.
2. **Containerized Environments**: Headless browsers run in isolated Docker containers, ensuring consistent environments and preventing "it works on my machine" issues.
3. **Thread-Safe Data**: Test data and reporting mechanisms are designed to safely handle concurrent read/writes.
4. **Dynamic Driver Instantiation**: WebDrivers are spun up and torn down for each thread autonomously without collisions.

## 🚀 Getting Started
1. Start the Dockerized Grid: `docker-compose up -d`
2. Install dependencies: `pip install -r requirements.txt`
3. Execute the tests in parallel (e.g., using 4 workers): `pytest -n 4 tests/`

> *"I don't just automate tests. I build testers."* — Teddy Lioner
