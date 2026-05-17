from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/fast")
def fast():
    return "Fast response"

@app.route("/slow")
def slow():
    # Simulate a slow backend (2-5 seconds)
    delay = random.uniform(2, 5)
    time.sleep(delay)
    return f"Slow response after {delay:.2f}s"