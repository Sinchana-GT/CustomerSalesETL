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


