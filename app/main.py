from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Secure Authentication System is running!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')