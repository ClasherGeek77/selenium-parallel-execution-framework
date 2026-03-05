import subprocess
import sys
import argparse
import os

def run_command(cmd: str):
    print(f"Executing: {cmd}")
    return subprocess.run(cmd, shell=True)

def start_grid():
    run_command("docker-compose up -d")

def stop_grid():
    run_command("docker-compose down")

def run_tests(parallel: int = 4, env: str = "local"):
    os.environ["TEST_ENV"] = env
    cmd = f"pytest -n {parallel} --alluredir=allure-results tests/"
    run_command(cmd)

def main():
    parser = argparse.ArgumentParser(description="Selenium Framework Sandbox CLI")
    parser.add_argument("action", choices=["up", "down", "test", "report"])
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--env", type=str, default="local")
    
    args = parser.parse_args()
    
    if args.action == "up":
        start_grid()
    elif args.action == "down":
        stop_grid()
    elif args.action == "test":
        run_tests(args.workers, args.env)
    elif args.action == "report":
        run_command("allure serve allure-results")

if __name__ == "__main__":
    main()
