from flask import Flask

app = Flask(__name__)

@app.route('/lab2')
def say_hello():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def moja_strona():
    return "To jest moja strona!"

if __name__ == '__main__':
    app.run()
