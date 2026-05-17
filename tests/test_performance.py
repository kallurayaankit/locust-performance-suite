import subprocess
import csv
import os
import pytest

SLA_P95_MS = 60000  # Maximum allowed 95th percentile latency in milliseconds

def test_locust_sla():
    # Create reports directory if not exists
    os.makedirs("reports", exist_ok=True)

    # Run Locust headless
    cmd = [
        "locust",
        "-f", "tests/locustfile.py",
        "--headless",
        "--host", "http://localhost:5000",
        "-u", "10",          # number of users
        "-r", "2",           # spawn rate
        "-t", "30s",         # run time
        "--csv", "reports/stats",
        "--html", "reports/locust_report.html"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    # Locust returns 0 even if requests fail, but we can check stats

    # Parse the stats CSV (the file reports/stats_stats.csv)
    stats_file = "reports/stats_stats.csv"
    if not os.path.exists(stats_file):
        pytest.fail("Locust stats file not found")

    with open(stats_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Name"] == "Aggregated":
                p95 = float(row["95%"])
                print(f"Aggregated p95 latency: {p95} ms")
                assert p95 <= SLA_P95_MS, f"p95 latency {p95} ms exceeds SLA of {SLA_P95_MS} ms"
                return
    pytest.fail("Aggregated row not found in stats")