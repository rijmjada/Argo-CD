from flask import Flask
import logging
from datetime import datetime
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    pod_name = os.getenv("HOSTNAME", "unknown-pod")
    path = '/app/data/visits.log'
    with open(path, 'a') as f:
        f.write(f"Visit at {datetime.now()} from pod {pod_name}\n")
    return f"Hello from Flask! Served by pod: {pod_name}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
