import fetcher, romanov, tweety
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_cnn')
def fetch_cnn():
    return romanov.run()

@app.route('/fetch_twitter')
def fetch_twitter():
    return tweety.run()

@app.route('/error')
def error():
    return "An unknown error has occurred. Please reload the desired webpage"

if __name__ == "__main__":
    app.run(debug=True)
