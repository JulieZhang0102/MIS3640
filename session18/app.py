from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/name')
def hello_world(name=None):
    if name:
        return f'Hello, {name}'
    else:
        return 'Hello World!'