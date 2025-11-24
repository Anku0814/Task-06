
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # 1. Connect to SQLite database
    conn = sqlite3.connect("sales_data.db")

    # 2. Define SQL query to get total quantity and revenue by product
    query = '''
    SELECT 
        product, 
        SUM(quantity) AS total_qty,
        SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
    '''

    # 3. Load query result into pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # 4. Close the connection
    conn.close()

    # 5. Print basic summary to console
    print("=== Basic Sales Summary by Product ===")
    print(df)

    # 6. Plot simple bar chart of revenue by product
    plt.figure(figsize=(8, 5))
    plt.bar(df["product"], df["revenue"])
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.title("Revenue by Product")
    plt.tight_layout()

    # Save the chart
    plt.savefig("sales_revenue_bar.png")
    plt.show()

if __name__ == "__main__":
    main()
