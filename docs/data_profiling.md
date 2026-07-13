# Data Profiling Report

### DataSet Summary 


| Dataset | Status | Main Finding |
|----------|----------|----------|
| Customers | ✅ Complete | Clean dataset |
| Geolocation | ✅ Complete | 261,831 duplicate rows |
| Orders | ✅ Complete | Business-valid nulls |
| Order Items | ✅ Complete | Clean dataset |
| Payments | ✅ Complete | Multiple payments per order |
| Reviews | ✅ Complete | Comments are optional |
| Products | ✅ Complete | 610 products missing metadata |
| Sellers | ✅ Complete | Clean dataset |
| Product Category Translation | ✅ Complete | Lookup table |


================================================================================
DATASET: CUSTOMERS
================================================================================

Purpose:
- Customer information

Shape:
- Rows: 99,441
- Columns: 5

Columns:
- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

Null Values:
- None

Duplicate Records:
- 0

Observations:
- Clean dataset
- No null values
- No duplicate records

ETL Decision:
- No action required

================================================================================
DATASET: GEOLOCATION
================================================================================

Purpose:
- Customer location information

Shape:
- Rows: 1,000,163
- Columns: 5

Null Values:
- None

Duplicate Records:
- 261,831

Unique Records:
- 738,332

Observations:
- Large number of duplicate records detected

ETL Decision:
- Investigate duplicate business meaning
- Do not remove duplicates yet

================================================================================
DATASET: ORDERS
================================================================================

Purpose:
- One row represents one customer order

Shape:
- Rows: 99,441
- Columns: 8

Duplicate Records:
- 0

Null Values:

1. order_approved_at
   - Null Count: 160

   Status Distribution:
   - canceled: 141
   - delivered: 14
   - created: 5

   Observation:
   - Mostly valid business nulls
   - Delivered records require investigation

2. order_delivered_carrier_date
   - Null Count: 1783

   Status Distribution:
   - unavailable: 609
   - canceled: 550
   - invoiced: 314
   - processing: 301
   - created: 5
   - approved: 2
   - delivered: 2

   Observation:
   - Mostly business-valid
   - Delivered records require investigation

3. order_delivered_customer_date
   - Null Count: 2965

   Status Distribution:
   - shipped: 1107
   - canceled: 619
   - unavailable: 609
   - invoiced: 314
   - processing: 301
   - delivered: 8
   - created: 5
   - approved: 2

   Observation:
   - Most nulls are expected
   - Delivered records require investigation

Overall Conclusion:
- Majority of null values are valid business scenarios.
- Small number of delivered orders contain missing timestamps.

ETL Decision:
- No cleaning yet
- Investigate suspicious delivered records 



================================================================================
DATASET: PAYMENTS
================================================================================

Purpose:
- One row represents a payment transaction for an order.

Shape:
- Rows: 103,886
- Columns: 5

Columns:
- order_id
- payment_sequential
- payment_type
- payment_installments
- payment_value

Null Values:
- 0

Duplicate Records:
- 0

Business Analysis
-----------------

Total Payment Records:
- 103,886

Unique Orders:
- 99,440

Observation:
- Number of payment records exceeds the number of unique orders.
- A single order can have multiple payment transactions.

Payment Types:

- credit_card: 76,795
- boleto: 19,784
- voucher: 5,775
- debit_card: 1,529
- not_defined: 3

Observation:
- Credit card is the dominant payment method.
- Three records have payment type as 'not_defined'.

Payment Installments:

- Minimum: 0
- 25%: 1
- Median (50%): 1
- 75%: 4
- Maximum: 24
- Average: 2.85

Observation:
- Most customers use one installment.
- 75% of payments use four or fewer installments.
- Some records have 0 installments and require investigation.

Payment Value:

- Minimum: 0
- Average: 154.10
- Median: 100.00
- Maximum: 13,664.08

Observation:
- Some transactions have payment value equal to 0.
- High-value transactions exist.
- Requires business validation for zero-value payments.

Overall Conclusion:
- Dataset is clean from a data quality perspective.
- No null values detected.
- No duplicate records detected.
- Contains important business insights regarding customer payment behavior.

ETL Decision:
- No cleaning required currently.
- Investigate:
  - payment_installments = 0
  - payment_value = 0
  - payment_type = 'not_defined'

================================================================================
DATASET: ORDER_ITEMS
================================================================================

Purpose:
- One row represents one product within an order.

Shape:
- Rows: 112,650
- Columns: 7

Columns:
- order_id
- order_item_id
- product_id
- seller_id
- shipping_limit_date
- price
- freight_value

Null Values:
- 0

Duplicate Records:
- 0

Review Data Analysis
-----------------------

Review Distribution:

- 1 Star: 11,424
- 2 Stars: 3,151
- 3 Stars: 8,179
- 4 Stars: 19,142
- 5 Stars: 57,328

Observations:
- 5-star reviews account for the majority of ratings.
- Customer satisfaction appears to be generally high.
- Low-rated reviews represent a smaller proportion of total reviews.

Review Statistics:

- Average Rating: 4.09
- Median Rating: 5
- Minimum Rating: 1
- Maximum Rating: 5

Observations:
- The average rating is above 4.
- Half of all reviews have a rating of 5.
- Ratings are skewed toward positive feedback.

Review Comment Analysis:

Rows with Null Review Comments:

- 5 Stars: 36,774
- 4 Stars: 13,166
- 3 Stars: 4,622
- 2 Stars: 1,006
- 1 Star: 2,679

Observations:
- Many customers submit ratings without written comments.
- Missing comments are a valid business scenario.
- Customers are more likely to leave only a rating when satisfied.
- Comment fields appear optional.

Conclusion:
- The Reviews dataset is healthy.
- Null review comments should be retained.
- Review scores provide valuable customer satisfaction insights.

================================================================================
DATASET: PRODUCTS
================================================================================

Purpose:
- One row represents one product.

Shape:
- Rows: 32,951
- Columns: 9

Duplicate Records:
- 0

Null Values:

Product Metadata:
- product_category_name: 610
- product_name_lenght: 610
- product_description_lenght: 610
- product_photos_qty: 610

Product Dimensions:
- product_weight_g: 2
- product_length_cm: 2
- product_height_cm: 2
- product_width_cm: 2

Detailed Investigation:

Metadata Missing Products:
- 610 products are missing category and descriptive metadata.
- Physical dimensions are available for most of these products.

Dimension Missing Products:
- 2 products are missing all dimensional attributes.
- One of these products contains category information.
- One product is missing both metadata and dimensional information.

Observations:
- Missing values are concentrated in specific products.
- Data quality issue appears to be product-specific rather than dataset-wide.

ETL Decision:
- Do not remove records.
- Further investigation required during transformation phase.

================================================================================
DATASET: SELLERS
================================================================================

Purpose:
- One row represents one seller.

Shape:
- Rows: 3,095
- Columns: 4

Null Values:
- 0

Duplicate Records:
- 0

Primary Key Validation:

Unique seller_id:
- 3,095

Total Rows:
- 3,095

Observation:
- seller_id is unique.
- seller_id can be treated as the primary key.

Relationships:
- seller_id → Order Items Dataset

Overall Conclusion:
- Dataset is clean.
- No data quality issues identified.

ETL Decision:
- No cleaning required.

================================================================================
DATASET: PRODUCT_CATEGORY_TRANSLATION
================================================================================

Purpose:
- Maps Portuguese product categories to English categories.

Shape:
- Rows: 71
- Columns: 2

Columns:
- product_category_name
- product_category_name_english

Null Values:
- 0

Duplicate Records:
- 0

Unique Categories:
- 71

Observations:
- One-to-one mapping between Portuguese and English category names.
- Dataset is complete and clean.
- Suitable for enrichment during transformation phase.

Relationship:
- product_category_name → Products Dataset

ETL Decision:
- No cleaning required.
- Use during transformation to translate category names to English.