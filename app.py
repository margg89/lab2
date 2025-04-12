from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        num1 = float(request.args.get("num1", 0))
        num2 = float(request.args.get("num2", 0))

        result = 1 if (num1 + num2) > 5.8 else 0

        return jsonify({
        "prediction": result,
        "features": {
        "num1": num1,
        "num2": num2
    }
})

    except (ValueError, TypeError):
        return jsonify({"error": "Błędne dane wejściowe"}), 400

if __name__ == '__main__':
    app.run()
