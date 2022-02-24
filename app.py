from flask import Flask
app = Flask(__name__)
@app.route('/what',)
def What():
    return 'WAAAAAT'

@app.route('/')
def hello_world():
    return 'Hello World'