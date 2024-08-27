from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is to test web app on the Virtual Machine"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
