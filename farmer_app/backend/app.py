from flask import Flask
from routes import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def home():
    return "Welcome to the Farmer App"

if __name__ == '__main__':
    app.run(debug=True)
