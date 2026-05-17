# Locust Performance Test Suite

![CI](https://github.com/kallurayaankit/locust-performance-suite/actions/workflows/ci.yml/badge.svg)

Performance test suite that uses **Locust** to simulate load against a Flask app and verifies SLA thresholds (p95 latency). If latency exceeds the limit, the test fails — proving performance regressions are caught automatically.

## What it does
- A simple Flask app serves fast and slow endpoints.
- Locust spawns virtual users that hit both endpoints.
- A pytest test runs Locust headless, parses the statistics, and asserts that the 95th percentile latency is below a defined SLA (2000 ms).
- An HTML report is generated for both Locust and pytest.
- CI/CD runs the entire pipeline on every push and daily.
-The performance test runs automatically in CI and fails if the p95 latency exceeds the SLA.

## How to run locally

1. Start the target Flask app in one terminal:
   ```bash
   cd app
   pip install -r requirements.txt
   python app.py