import subprocess
import json
import re

def run_tests_and_generate_results():
    result = subprocess.run(
        ["python", "-m", "pytest", "-v"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    results = {}

    # Example line:
    # tests/test_app.py::test_login PASSED
    lines = output.split("\n")

    for line in lines:
        if "test_" in line and ("PASSED" in line or "FAILED" in line):
            parts = line.strip().split("::")
            if len(parts) > 1:
                test_part = parts[1]
                test_name = test_part.split()[0]

                if "PASSED" in line:
                    results[test_name] = "PASS"
                elif "FAILED" in line:
                    results[test_name] = "FAIL"

    with open("ci_results/results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("✅ CI results generated from pytest!")