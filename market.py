from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def maarket_page():
    items = [
        {'id': 1, 'name': 'phone','barcode' : '893211235466', 'price': 1000},
        {'id': 2, 'name': 'laptop','barcode' : '893211235467', 'price': 2000},
        {'id': 3, 'name': 'tablet','barcode' : '893211235468', 'price': 1500}
    ]
    return render_template("market.html", items=items)