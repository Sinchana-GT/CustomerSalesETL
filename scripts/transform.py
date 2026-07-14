import pandas as pd

# Load all source datasets into memory
datasets = {
    "customers": pd.read_csv("../data/olist_customers_dataset.csv"),
    "geolocation": pd.read_csv("../data/olist_geolocation_dataset.csv"),
    "orders": pd.read_csv("../data/olist_orders_dataset.csv"),
    "order_items": pd.read_csv("../data/olist_order_items_dataset.csv"),
    "payments": pd.read_csv("../data/olist_order_payments_dataset.csv"),
    "reviews": pd.read_csv("../data/olist_order_reviews_dataset.csv"),
    "products": pd.read_csv("../data/olist_products_dataset.csv"),
    "sellers": pd.read_csv("../data/olist_sellers_dataset.csv"),
    "product_category_name": pd.read_csv("../data/product_category_name_translation.csv"),
}

# Select datasets required for relationship validation
order = datasets["orders"]
order_items = datasets["order_items"]
payments = datasets["payments"]

# ------------------------------------------------------------------
# Relationship Validation
# Goal:
# Verify how Orders, Order Items and Payments are related.
# ------------------------------------------------------------------

print("Orders unique order_id:", order["order_id"].nunique())
print("Orders Items unique order_id:", order_items["order_id"].nunique())
print("Payments unique order_id:", payments["order_id"].nunique())

# ------------------------------------------------------------------
# Find orders that exist in Orders but are missing in Order Items.
#
# Business Question:
# Are there orders that never received product records?
#
# Expected Reasons:
# - cancelled orders
# - unavailable orders
# - incomplete orders
# ------------------------------------------------------------------

missing_order_items = order[~order["order_id"].isin(order_items["order_id"])]
print(missing_order_items.shape)
print(missing_order_items["order_status"].value_counts())

# ------------------------------------------------------------------
# Find orders that exist in Orders but are missing in Payments.
#
# Business Question:
# Did every order receive a payment transaction?
# ------------------------------------------------------------------

missing_payments = order[~order["order_id"].isin(payments["order_id"])]
print(missing_payments)
print(missing_payments["order_status"].value_counts())

# ------------------------------------------------------------------
# First Transformation
#
# Merge Orders and Order Items using order_id.
#
# Why?
# Orders contain:
# - customer information
# - order status
# - order dates
#
# Order Items contain:
# - products
# - sellers
# - prices
#
# After merging, each row represents:
# "A product sold within an order"
# ------------------------------------------------------------------

sales_v1 = order.merge(
    order_items,
    on="order_id",
    how="inner"
)

print("\nSales V1 Shape:")
print(sales_v1.shape)

print("\nSales V1 Columns:")
print(sales_v1.columns.tolist())

print("\nFirst 5 Rows:")
print(sales_v1.head())

# ------------------------------------------------------------------
# Validate relationship between Sales_V1 and Payments.
#
# Goal:
# Check whether every order in Sales_V1 has a payment record
# before performing the next merge.
# ------------------------------------------------------------------

print("\nSales_V1 Unique Orders:")
print(sales_v1["order_id"].nunique())

print("\nPayments Unique Orders:")
print(payments["order_id"].nunique())

# ------------------------------------------------------------------
# Validate whether every order in Sales_V1 has a payment record.
#
# Business Question:
# If we merge Sales_V1 with Payments using an INNER JOIN,
# will any orders be lost?
#
# We compare Sales_V1 order_id values against Payments order_id values.
# Orders that do not exist in Payments will be excluded during the merge.
# ------------------------------------------------------------------

missing_payments_in_sales = sales_v1[
    ~sales_v1["order_id"].isin(payments["order_id"])
]

print("\nOrders in Sales_V1 missing from Payments:")
print(missing_payments_in_sales.shape)

# Display a sample if any records are missing
print(missing_payments_in_sales.head())

# ------------------------------------------------------------------
# Result Analysis
#
# Although 3 rows are returned, they belong to the same order_id.
#
# This happens because Sales_V1 contains one row per product within an order.
#
# Therefore:
# 1 missing order
# becomes
# 3 rows if the order contains 3 products.
# ------------------------------------------------------------------

print("\nUnique Missing Orders:")
print(missing_payments_in_sales["order_id"].nunique())

# ------------------------------------------------------------------
# Second Transformation
#
# Merge Sales_V1 with Payments.
#
# Purpose:
# Add payment information to each sales record.
# ------------------------------------------------------------------

sales_v2 = sales_v1.merge(
    payments,
    on="order_id",
    how="inner"
)

print("\nSales V2 Shape:")
print(sales_v2.shape)

print("\nSales V2 Columns:")
print(sales_v2.columns.tolist())

# ------------------------------------------------------------------
# Sales_V2 contains order information, product information and
# payment information.
#
# Row count increased after the merge because some orders contain
# multiple payment records.
#
# One order may have:
# - multiple products
# - multiple payments
#
# This creates additional rows after joining.
# ------------------------------------------------------------------
print(sales_v2["order_id"].nunique())
print(payments["order_id"].nunique())
print(order["order_id"].nunique())

# ------------------------------------------------------------------
# Merge Validation Result
#
# Original Orders                : 99,441
# Orders after Order Items Join  : 98,666----> 99,441 - 775
# Orders after Payments Join     : 98,665----> 98,666 - 1
#
# Lost Orders:
# - 775 orders missing in Order Items
# - 1 order missing in Payments
#
# INNER JOIN behavior matches expectations.
# ------------------------------------------------------------------

# Create a new business metric by adding product price and shipping cost
sales_v2["total_item_value"] = (sales_v2["price"]+ sales_v2["freight_value"])

# Verify the calculation for a few records
print(sales_v2[["price", "freight_value", "total_item_value"]].head())

# Basic statistics for total item value
print(sales_v2["total_item_value"].describe())