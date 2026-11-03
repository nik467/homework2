import json
import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS shop_catalog;")

cursor.execute('''
    CREATE TABLE shop_catalog (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        price REAL,
        category_name TEXT
    );
''')

with open("catalog (4).json", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    product_name = item["product_name"]
    price = item["price"]
    category_name = item["category"]["name"]

    cursor.execute(
        "INSERT INTO shop_catalog (product_name, price, category_name) VALUES (?, ?, ?)",
        (product_name, price, category_name)
    )

conn.commit()
conn.close()