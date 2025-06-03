from sql_solution import extract_with_sql
import os
from config import DB_PATH
from db_create import create_db
from pandas_solution import extract_with_pandas

def main():
    # checking if the db exists
    if not os.path.exists(DB_PATH):
        print("creating DB")
        create_db()
    
    # checking if the output dir exists
    if not os.path.exists('output'):
        os.makedirs('output')
        print("Created output directory")
    

    print("Running SQL solution.")
    extract_with_sql()
    print("SQL solution completed and CSV generated.\n")

    print("Running Pandas solution.")
    extract_with_pandas()
    print("Pandas solution completed and CSV generated.")

if __name__ == "__main__":
    main()
