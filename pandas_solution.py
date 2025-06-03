import pandas as pd
from db_connector import get_connection
from config import PANDAS_CSV_OUTPUT_PATH, CSV_DELIMITER

def extract_with_pandas():
    with get_connection() as conn:
        df_customers = pd.read_sql_query("SELECT * FROM customers", conn)
        df_orders = pd.read_sql_query("SELECT * FROM orders", conn)
        df_items = pd.read_sql_query("SELECT * FROM items", conn)
        df_sales = pd.read_sql_query("SELECT * FROM sales", conn)

    merged = (
        df_sales
        .merge(df_orders, on="order_id")
        .merge(df_customers, on="customer_id")
        .merge(df_items, on="item_id")
    )

    filtered = merged[
        (merged["age"].between(18, 35)) &
        (merged["quantity"].notnull())
    ]

    grouped = (
        filtered.groupby(["customer_id", "age", "item_name"], as_index=False)
        .agg({"quantity": "sum"})
    )

    result = grouped[grouped["quantity"] > 0]
    result = result.rename(columns={
        "customer_id": "Customer",
        "age": "Age",
        "item_name": "Item",
        "quantity": "Quantity"
    })

    result.to_csv(PANDAS_CSV_OUTPUT_PATH, sep=CSV_DELIMITER, index=False)
