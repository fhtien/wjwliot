from flask import Flask
from flask import Blueprint

app = Flask(__name__)


@app.route('/')
def test():
    return "<h1>這是一個h1<h1/>"


if __name__ == '__main__':

    app.run()