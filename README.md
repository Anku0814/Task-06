
# Task 06 – Basic Sales Summary from SQLite using Python

This repository contains a simple solution for **Data Analytics Internship – Task 6: Get Basic Sales Summary from a Tiny SQLite Database using Python**.

## Files in this project

- `sales_data.db` – SQLite database with a single table `sales`.
- `task06_sales_summary.py` – Python script that connects to the database, runs SQL, prints a summary, and creates a bar chart.
- `sales_revenue_bar.png` – This file will be created after you run the script (bar chart of revenue by product).
- `README.md` – This explanation file.

## How to run

1. Make sure you have **Python 3** installed.
2. Install required Python libraries (if not already installed):

   ```bash
   pip install pandas matplotlib
   ```

3. Keep all files in the **same folder** (`sales_data.db` and `task06_sales_summary.py`).
4. Open a terminal/command prompt in that folder and run:

   ```bash
   python task06_sales_summary.py
   ```

5. The script will:
   - Connect to `sales_data.db`
   - Run a SQL query to calculate **total quantity** and **total revenue** for each product
   - Print the result as a pandas DataFrame
   - Create and save a bar chart as `sales_revenue_bar.png`

## SQL Query Used

```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
```

## Short Answers to Interview Questions

- **How did you connect Python to a database?**  
  Using `sqlite3.connect("sales_data.db")` to create a connection object.

- **What SQL query did you run?**  
  A `SELECT` query with `SUM(quantity)` and `SUM(quantity * price)` grouped by `product` to get total quantity and revenue per product.

- **What does GROUP BY do?**  
  It groups rows that have the same value in one or more columns (here, `product`) so aggregate functions like `SUM()` work per group.

- **How did you calculate revenue?**  
  In SQL as `SUM(quantity * price)` for each product.

- **How did you visualize the result?**  
  By using matplotlib to create a bar chart: products on the x-axis and revenue on the y-axis, then saving it as `sales_revenue_bar.png`.

- **What does pandas do in your code?**  
  It reads the SQL query result into a DataFrame, which makes it easier to print, inspect, and pass to plotting functions.

- **What’s the benefit of using SQL inside Python?**  
  You can combine the power of SQL for data extraction/aggregation with Python’s ecosystem (pandas, matplotlib) for analysis and visualization in a single workflow.

- **Could you run the same SQL query directly in DB Browser for SQLite?**  
  Yes, the same query can be executed directly in any SQLite tool (like DB Browser for SQLite). Python just automates it and lets us continue the analysis programmatically.
