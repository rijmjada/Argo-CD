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

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App - Pod Info</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                text-align: center;
                padding-top: 100px;
            }}
            .container {{
                background-color: #fff;
                display: inline-block;
                padding: 30px 50px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #007BFF;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello from Flask!</h1>
            <p>Served by pod: <strong>{pod_name}</strong></p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
