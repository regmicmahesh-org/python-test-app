from flask import Flask, request
import json

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
