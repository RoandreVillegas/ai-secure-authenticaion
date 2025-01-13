from flask import Flask
from routes import auth # Import Blueprint from routes.py

app = Flask(__name__)

app.register_blueprint(auth, url_prefix = '/auth')

@app.route('/')
def home():
    return "AI Secure Authentication System is running!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')