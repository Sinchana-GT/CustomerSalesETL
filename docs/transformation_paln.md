# Transformation Plan

## Fact Table

fact_sales

Source Tables:
- orders
- order_items
- payments

Key Columns:
- order_id
- customer_id
- product_id
- seller_id
- payment_type
- payment_value
- price
- freight_value

Derived Columns:
- total_sales = price + freight_value

---

## Dimension Tables

### dim_customer
Source:
- customers

### dim_product
Source:
- products
- product_category_translation

### dim_seller
Source:
- sellers

### dim_date
Source:
- order_purchase_timestamp