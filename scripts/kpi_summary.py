import pandas as pd
from sqlalchemy import create_engine

# Neon connection
engine = create_engine(
    "postgresql://neondb_owner:npg_ogntx9W3Bash@ep-small-glade-attvzk99-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

# KPI Queries
queries = {
    "Total Revenue": """
        SELECT ROUND(SUM(total_item_value)::numeric, 2)
        FROM fact_sales
    """,

    "Total Orders": """
        SELECT COUNT(DISTINCT order_id)
        FROM fact_sales
    """,

    "Total Customers": """
        SELECT COUNT(DISTINCT customer_unique_id)
        FROM fact_sales
    """,

    "Total Sellers": """
        SELECT COUNT(DISTINCT seller_id)
        FROM fact_sales
    """,

    "Top Payment Method": """
        SELECT payment_type
        FROM fact_sales
        GROUP BY payment_type
        ORDER BY COUNT(DISTINCT order_id) DESC
        LIMIT 1
    """,

    "Top Revenue Category": """
        SELECT product_category_name_english
        FROM fact_sales
        GROUP BY product_category_name_english
        ORDER BY SUM(total_item_value) DESC
        LIMIT 1
    """,

    "Top Revenue State": """
        SELECT customer_state
        FROM fact_sales
        GROUP BY customer_state
        ORDER BY SUM(total_item_value) DESC
        LIMIT 1
    """,

    "Top Customer State": """
        SELECT customer_state
        FROM fact_sales
        GROUP BY customer_state
        ORDER BY COUNT(DISTINCT customer_unique_id) DESC
        LIMIT 1
    """,

    "Average Orders Per Customer": """
        SELECT ROUND(
            AVG(order_count)::numeric,
            2
        )
        FROM (
            SELECT
                customer_unique_id,
                COUNT(DISTINCT order_id) AS order_count
            FROM fact_sales
            GROUP BY customer_unique_id
        ) customer_orders
    """
}

# Generate KPI Summary
kpi_data = []

for kpi_name, query in queries.items():
    value = pd.read_sql(query, engine).iloc[0, 0]

    kpi_data.append({
        "kpi_name": kpi_name,
        "kpi_value": value
    })

# Create DataFrame
kpi_summary = pd.DataFrame(kpi_data)

# Display KPIs
print("\nKPI Summary:")
print(kpi_summary)

# Export CSV
kpi_summary.to_csv(
    "../output/kpi_summary.csv",
    index=False
)

print("\nKPI summary exported successfully.")