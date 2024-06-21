from flask import Flask
from makeRequest import makeRequest

app = Flask(__name__)


@app.route("/")
def index():
    req = makeRequest()
    req.url += "/employees"
    req.get()
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
