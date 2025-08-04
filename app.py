from flask import Flask, request, jsonify

app = Flask(__name__)
orders = []

@app.route('/orders', methods=['GET', 'POST'])
def orders_endpoint():
    if request.method == 'POST':
        new_order = request.get_json()
        new_order['id'] = len(orders) + 1
        orders.append(new_order)
        return jsonify(new_order), 201
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)