# Customer Sales ETL Architecture

Source Layer
------------
Olist CSV Files

- Customers
- Orders
- Order Items
- Payments
- Products
- Geolocation

         |
         v

Extract Layer
-------------
Python
Pandas

         |
         v

Transform Layer
---------------
Data Cleaning
Data Validation
Duplicate Detection
Missing Value Analysis

         |
         v

Load Layer
----------
PostgreSQL

         |
         v

Reporting Layer
---------------
SQL Queries
Power BI Dashboards


DataSet Relationship
---------------------

Customers
    |
customer_id
    |
Orders
    |
order_id
    |
+-------------+
|             |
Payments   Order Items
               |
          +----+----+
          |         |
      Products   Sellers



## Source Datasets

- customers
- orders
- order_items
- payments
- products
- product_category_translation
- sellers

## ETL Flow

orders
    +
order_items
    ↓
sales_v1

sales_v1
    +
payments
    ↓
sales_v2

sales_v2
    +
products
    ↓
sales_v3

sales_v3
    +
product_category_translation
    ↓
sales_v4

sales_v4
    +
sellers
    ↓
sales_v5

sales_v5
    +
customers
    ↓
Sales_V6

sales_v6 (fact_sales)
    ↓
fact_sales.csv
    ↓
Neon PostgreSQL
    ↓
fact_sales


