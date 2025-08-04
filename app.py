from flask import Flask, request, jsonify
import random

app = Flask(__name__)

orders = []
example_orders = [
    {"destination": "Japan", "start_date": "2025-10-01", "end_date": "2025-10-14"},
    {"destination": "Italy", "start_date": "2025-11-01", "end_date": "2025-11-10"},
    {"destination": "Spain", "start_date": "2025-09-15", "end_date": "2025-09-25"},
    {"destination": "France", "start_date": "2025-12-01", "end_date": "2025-12-10"}
]

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "Welcome to the API! Try /orders"}), 200

@app.route('/orders', methods=['GET', 'POST'])
def orders_endpoint():
    if request.method == 'POST':
        new_order = request.get_json()
        new_order['id'] = len(orders) + 1
        orders.append(new_order)
        return jsonify(new_order), 201

    if not orders:
        sample = random.sample(example_orders, k=2)
        for item in sample:
            item = item.copy()
            item['id'] = len(orders) + 1
            orders.append(item)

    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
