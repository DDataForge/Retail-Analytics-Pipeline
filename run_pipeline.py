import subprocess
import sys

def run_step(script):
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"Error running {script}")
        exit(1)

print("Running ETL pipeline...")
run_step("src/etl.py")

print("Loading data into database...")
run_step("src/database.py")

print("Running forecasting model...")
run_step("src/forecasting.py")

print("Pipeline executed successfully!")