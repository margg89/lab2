from flask import Flask, request

app = Flask(__name__)

@app.route('/lab2')
def say_hello():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def moja_strona():
    return "To jest moja strona!"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get("name", "")
    if name:
        response = f"Hello {name}"
    else:
        response = "Hello"
    return response

if __name__ == '__main__':
    app.run()
