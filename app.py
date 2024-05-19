from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/currencies')
def get_currencies():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')  # Utiliser USD comme base par défaut
    if response.status_code == 200:
        data = response.json()
        currencies = list(data['rates'].keys())
        return jsonify(currencies)
    else:
        return jsonify({"error": "Failed to fetch currencies"}), 500    

@app.route('/convert', methods=['GET'])
def convert_currency():
    amount = float(request.args.get('amount', 1))
    from_currency = request.args.get('from', 'USD')
    to_currency = request.args.get('to', 'EUR')
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch exchange rates"}), 500
    rates = response.json().get('rates', {})
    to_rate = rates.get(to_currency)
    if not to_rate:
        return jsonify({"error": "Invalid currency code"}), 400
    converted_amount = amount * to_rate
    return jsonify({"converted_amount": round(converted_amount, 2)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

