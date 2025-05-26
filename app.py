from flask import Flask
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    path = '/app/data/visits.log'
    with open(path, 'a') as f:
        f.write(f"Visit at {datetime.now()}\n")
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
