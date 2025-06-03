from db_connector import get_connection
import csv
from config import SQL_CSV_OUTPUT_PATH, CSV_DELIMITER

def extract_with_sql():
    query = """
    SELECT
        c.customer_id AS Customer,
        c.age AS Age,
        i.item_name AS Item,
        SUM(s.quantity) AS Quantity
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN sales s ON o.order_id = s.order_id
    JOIN items i ON s.item_id = i.item_id
    WHERE c.age BETWEEN 18 AND 35 AND s.quantity IS NOT NULL
    GROUP BY c.customer_id, i.item_name
    HAVING SUM(s.quantity) > 0
    ORDER BY c.customer_id, i.item_name;
    """
    
    with get_connection() as conn:
        cursor = conn.cursor()
        rows = cursor.execute(query).fetchall()

    with open(SQL_CSV_OUTPUT_PATH, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=CSV_DELIMITER)
        writer.writerow(["Customer", "Age", "Item", "Quantity"])
        for row in rows:
            writer.writerow(row)
