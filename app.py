from flask import Flask, request
import json
import pika



app = Flask(__name__, static_folder='')

items = []

@app.route('/')
def index():
    print("Hello")
    return app.send_static_file("index.html")

@app.route('/headers')
def print_headers():
    res = json.dumps(dict(request.headers))
    return res

@app.route('/add')
def add_a_number():
    items.append(len(items) + 1)
    return f"{len(items)} added to the list."

@app.route('/view')
def view_all_numbers():
    res = "<h1>Items</h1>"
    for item in items:
        res += f"<h5>{item}</h5>"

    return res

@app.route('/otp', methods=['POST'])
def send_otp():

    number: str = request.form.get('number')
    routing_key = ""

    if number.startswith('91'):
        routing_key="india"
    elif number.startswith('977'):
        routing_key='nepal'
    
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='10.6.0.7'))
    channel = conn.channel()

    channel.basic_publish('ex.otp', routing_key, number.encode('utf-8'))
    channel.close()
    conn.close()
    return "<h1> OTP Request sent to API Gateway!</h1>"