from db_connector import get_connection

def create_db():
    with open("datadump.sql", "r") as f:
        schema = f.read()

    conn = get_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()