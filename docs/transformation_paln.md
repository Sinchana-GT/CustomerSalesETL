# Transformation Plan

## Objective

Build a Sales Analytics Data Model by transforming and combining Olist source datasets into a business-friendly structure suitable for PostgreSQL and Power BI.

---

# Fact Table

## fact_sales

Purpose:
- Store sales transactions at the product level.
- Each row represents one product sold within an order.

Source Tables:
- orders
- order_items
- payments

Key Columns:
- order_id
- customer_id
- product_id
- seller_id

Order Information:
- order_status
- order_purchase_timestamp
- order_approved_at
- order_delivered_carrier_date
- order_delivered_customer_date
- order_estimated_delivery_date

Product Information:
- product_id
- seller_id

Payment Information:
- payment_type
- payment_installments
- payment_value

Sales Metrics:
- price
- freight_value

Derived Columns:
- total_item_value = price + freight_value

Current Transformations Completed:

Transformation 1:
orders + order_items

Result:
- Sales_V1
- Shape: (112650, 14)

Transformation 2:
Sales_V1 + payments

Result:
- Sales_V2
- Shape: (117601, 18)

Transformation 3:
Derived Metric

- total_item_value

Formula:

total_item_value = price + freight_value

Validation:
- Minimum Value: 6.08
- Average Value: 140.87
- Median Value: 92.12
- Maximum Value: 6929.31

---

# Dimension Tables

## dim_customer

Purpose:
- Store customer information.

Source:
- customers

Key:
- customer_id

Columns:
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

---

## dim_product

Purpose:
- Store product attributes.

Source:
- products
- product_category_translation

Key:
- product_id

Columns:
- product_category_name
- product_category_name_english
- product_weight_g
- product_length_cm
- product_height_cm
- product_width_cm

Planned Enrichment:
- Translate Portuguese category names into English.

Known Data Issues:
- 610 products missing metadata.
- 2 products missing dimensions.

---

## dim_seller

Purpose:
- Store seller information.

Source:
- sellers

Key:
- seller_id

Columns:
- seller_zip_code_prefix
- seller_city
- seller_state

Validation:
- seller_id is unique.
- No null values.
- No duplicate records.

---

## dim_date

Purpose:
- Support time-based reporting.

Source:
- order_purchase_timestamp

Derived Attributes:
- year
- quarter
- month
- month_name
- day
- weekday

Business Use Cases:
- Monthly Sales Analysis
- Quarterly Revenue Analysis
- Year-over-Year Comparisons

---

# Relationship Model

customers
    │
customer_id
    │
orders
    │
order_id
    │
+---------------+
|               |
payments    order_items
                 │
        +--------+--------+
        |                 |
     products         sellers

---

# Data Quality Considerations

Orders:
- Most null values are valid business scenarios.
- Delivered orders with missing timestamps require investigation.

Payments:
- payment_installments = 0 requires validation.
- payment_value = 0 requires validation.
- payment_type = not_defined requires validation.

Products:
- 610 products missing metadata.
- 2 products missing dimensions.

Geolocation:
- 261,831 duplicate records identified.
- Duplicate business meaning requires validation.

---

# Next Steps

1. Validate Product relationships.
2. Merge Products into Sales_V2.
3. Merge Category Translation data.
4. Validate Product null values after merge.
5. Merge Seller information.
6. Create final fact_sales dataset.
7. Load transformed tables into PostgreSQL.
8. Create reporting queries.
9. Build Power BI dashboard.

Current Status

✅ Orders + Order Items Merge
✅ Payments Merge
✅ Products Merge
✅ Product Category Translation Merge
✅ Sellers Merge
✅ Customers Merge
✅ Fact Sales Dataset Created

Final Dataset:
- Sales_V6
- 117,601 Rows
- 35 Columns
