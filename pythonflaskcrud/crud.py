# app.py
import pymysql
from pymysql.cursors import DictCursor

# Database configuration
DB_HOST = 'sbdemodb.cdtqd6jgia7i.ap-south-1.rds.amazonaws.com'
DB_USER = 'admin'
DB_PASSWORD = 'admin1234'
DB_NAME = 'sbdemodb'

# Connect to the database
connection = pymysql.connect(host=DB_HOST,
                             user=DB_USER,
                             password=DB_PASSWORD,
                             database=DB_NAME,
                             cursorclass=DictCursor)

def create_product(name, supplier, price):
    with connection.cursor() as cursor:
        sql = "INSERT INTO product (name, supplier, price) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, supplier, int(price)))
        connection.commit()

def get_product(product_id):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM product WHERE id = %s"
        cursor.execute(sql, (product_id,))
        result = cursor.fetchone()
        return result

def update_product(product_id, name, supplier, price):
    with connection.cursor() as cursor:
        sql = "UPDATE product SET name = %s, supplier = %s, price = %s WHERE id = %s"
        cursor.execute(sql, (name, supplier, int(price), product_id))
        connection.commit()

def delete_product(product_id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM product WHERE id = %s"
        cursor.execute(sql, (product_id,))
        connection.commit()

def list_products():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

# Example usage
if __name__ == "__main__":
    # Create a new product
    create_product('Example Product', 'Example Supplier', 1000)
    
    # List all products
    products = list_products()
    print(products)
    
    # Get a specific product
    product = get_product(1)  # Assuming the product with ID 1 exists
    print(product)
    
    # Update a product
    update_product(1, 'Updated Product', 'Updated Supplier', 1500)
    
    # Delete a product
    delete_product(1)