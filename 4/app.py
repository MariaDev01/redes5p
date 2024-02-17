from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá, mundo! Esta é uma aplicação web em Python.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
