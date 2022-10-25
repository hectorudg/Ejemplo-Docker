# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola Mundo!"

app.run(host="0.0.0.0")