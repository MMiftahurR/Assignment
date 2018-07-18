# Import library flask
from flask import Flask

# Inisiasi app flask
app = Flask("Hello Web Apps")

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!!"

@app.route('/hai', methods=['GET'])
def hai():
    return "Haii!!"

app.run(port=7777)