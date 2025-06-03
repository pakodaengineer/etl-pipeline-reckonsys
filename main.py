from sql_solution import extract_with_sql
from pandas_solution import extract_with_pandas

def main():
    print("Running SQL solution.")
    extract_with_sql()
    print("SQL solution completed and CSV generated.\n")

    print("Running Pandas solution.")
    extract_with_pandas()
    print("Pandas solution completed and CSV generated.")

if __name__ == "__main__":
    main()
