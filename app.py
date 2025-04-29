from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello():
    app.logger.info("Hello endpoint was called from %s", request.remote_addr)
    return "Hello from Python app with logs!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
