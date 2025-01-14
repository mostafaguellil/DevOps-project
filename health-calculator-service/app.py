from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')

    if height is None or weight is None:
        return jsonify({"error": "Please provide both height (meters) and weight (kg)."}), 400

    try:
        bmi_result = calculate_bmi(height, weight)
        return jsonify({"bmi": round(bmi_result, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')

    if None in [height, weight, age, gender]:
        return jsonify({"error": "Please provide height (cm), weight (kg), age, and gender."}), 400

    if gender.lower() not in ['male', 'female']:
        return jsonify({"error": "Gender must be 'male' or 'female'."}), 400

    try:
        bmr_result = calculate_bmr(height, weight, age, gender.lower())
        return jsonify({"bmr": round(bmr_result, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)