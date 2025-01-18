from FoodProduct import FoodProduct
from FoodProduct import ProductCategory
from datetime import datetime,timedelta
import sqlite3

conn = sqlite3.connect("products.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL,
    production_date DATETIME NOT NULL,
    expiration_date DATETIME NOT NULL,
    remaining INTEGER NOT NULL
);
''')
conn.commit()


def insert_product(my_cursor, product_insert: FoodProduct):
    query = '''
    INSERT INTO Products (name, price, category, production_date, expiration_date, remaining)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    my_cursor.execute(query, (product_insert.name,
                              product_insert.price,
                              product_insert.category.value,
                              product_insert.production_date.strftime('%Y-%m-%d %H:%M:%S'),
                              product_insert.expiration_date.strftime('%Y-%m-%d %H:%M:%S'),
                              product_insert.remaining
                              ))
    my_cursor.connection.commit()

def get_products(my_cursor) -> list[FoodProduct]:
    result = my_cursor.execute('''
        SELECT * FROM Products
    ''')
    result_products = []
    for product in result.fetchall():
        one_row = dict(product)
        print(one_row)
        product = FoodProduct(
            name=one_row['name'],
            price=float(one_row['price']),
            category=ProductCategory(one_row['category']),
            production_date=datetime.strptime(one_row['production_date'], '%Y-%m-%d %H:%M:%S'),
            expiration_date=datetime.strptime(one_row['expiration_date'], '%Y-%m-%d %H:%M:%S'),
            product_id=one_row['id']
        )
        result_products.append(product)
    return result_products

if __name__ == '__main__':

    # Clear existing data (optional, use with caution)
    cursor.execute("DELETE FROM Products")
    conn.commit()

    product1 = FoodProduct(
        name="Milk",
        price=12.5,
        category=ProductCategory.DAIRY,
        production_date=datetime.now() - timedelta(days=5),
        expiration_date=datetime.now() + timedelta(days=10)
    )

    product2 = FoodProduct(
        name="Steak",
        price=85.0,
        category=ProductCategory.MEAT,
        production_date=datetime.now() - timedelta(days=2),
        expiration_date=datetime.now() + timedelta(days=14)
    )

    product3 = FoodProduct(
        name="Tofu",
        price=22.0,
        category=ProductCategory.PARVE,
        production_date=datetime.now() - timedelta(days=7),
        expiration_date=datetime.now() + timedelta(days=20)
    )

    product4 = FoodProduct(
        name="Cheese",
        price=40.0,
        category=ProductCategory.DAIRY,
        production_date=datetime.now() - timedelta(days=10),
        expiration_date=datetime.now() + timedelta(days=5)
    )

    product5 = FoodProduct(
        name="Chicken",
        price=60.0,
        category=ProductCategory.MEAT,
        production_date=datetime.now() - timedelta(days=3),
        expiration_date=datetime.now() + timedelta(days=12)
    )

    insert_product(cursor,product1)
    insert_product(cursor,product2)
    insert_product(cursor,product3)
    insert_product(cursor,product4)
    insert_product(cursor,product5)

    product_list = get_products(cursor)
    print(product_list)