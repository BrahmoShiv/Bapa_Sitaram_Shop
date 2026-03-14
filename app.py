from flask import Flask, request, jsonify,send_from_directory
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)

DB_FILE = 'orders.csv'
ADMIN_PASS = "bapa123" # Simple logic for Section 1: Discrete Math

@app.route('/')
def home():
    # This force-reads the file from the current directory
    try:
        return open('index.html').read()
    except Exception as e:
        return f"File not found. Current directory files: {os.listdir('.')}"
        
@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.json
    with open(DB_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data.get('product'), data.get('price'), data.get('category'), "Confirmed"])
    return jsonify({"message": "Order Securely Processed!"})

@app.route('/get_orders', methods=['GET'])
def get_orders():
    # Section 5: Search & Filter Algorithms
    search_query = request.args.get('search', '').lower()
    orders = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Filter logic
                if not search_query or search_query in row[0].lower():
                    orders.append({"item": row[0], "price": row[1], "cat": row[2]})
    return jsonify(orders)
if __name__ == '__main__':
    # Render provides a 'PORT' environment variable, usually 10000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
