from flask import Flask, render_template, request as incame_request

app = Flask(__name__)


@app.get('/')
def index():
    return 'Hello, World!'
