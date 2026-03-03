import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home Safety Bot</title>
        <style>
            body {
                background-color: #121212;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                color: #00ffcc;
            }
            button {
                padding: 12px 25px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                background-color: #00ffcc;
                cursor: pointer;
            }
            button:hover {
                background-color: #00ccaa;
            }
        </style>
    </head>
    <body>
        <h1>🏠 Home Safety Bot</h1>
        <p>Your system is running successfully.</p>
        <button onclick="alert('System Secure ✅')">
            Check System Status
        </button>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
