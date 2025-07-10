from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import pandas as pd
from utils.clustering import perform_kmeans
from utils.apriori import perform_apriori

app = Flask(__name__)
DB = "database.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, items TEXT);")

@app.route("/")
def index():
    items = ['Milk', 'Bread', 'Eggs', 'Cheese', 'Butter', 'Apples', 'Oranges', 'Chips', 'Soda', 'Basketball']
    return render_template("index.html", items=items)

@app.route("/submit", methods=["POST"])
def submit():
    selected_items = request.json.get("items")
    if not selected_items:
        return jsonify({"error": "No items selected"}), 400
    items_str = ",".join(selected_items)
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO transactions (items) VALUES (?);", (items_str,))
    return jsonify({"success": True})

@app.route("/mine")
def mine():
    with sqlite3.connect(DB) as conn:
        cursor = conn.execute("SELECT items FROM transactions")
        rows = cursor.fetchall()
    transactions = [row[0].split(",") for row in rows]
    if len(transactions) < 5:
        return "Please create at least 5 transactions."
    kmeans_result = perform_kmeans(transactions)
    apriori_result = perform_apriori(transactions)
    return render_template("results.html", kmeans=kmeans_result, rules=apriori_result)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)