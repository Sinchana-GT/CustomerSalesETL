# Customer Sales ETL - Project Notes

## Day 1 - Project Setup

Tasks Completed:
- Created project structure
- Created virtual environment
- Installed pandas
- Installed sqlalchemy
- Installed psycopg2-binary
- Downloaded Olist E-Commerce Dataset

Project Structure Created:
- data/
- scripts/
- logs/
- output/
- docs/

---

## Day 2 - Initial Data Profiling

Datasets Analyzed:
- Customers
- Geolocation

Key Findings:

Customers:
- Rows: 99,441
- Columns: 5
- Null Values: 0
- Duplicate Records: 0

Geolocation:
- Rows: 1,000,163
- Columns: 5
- Null Values: 0
- Duplicate Records: 261,831

Observations:
- Customers dataset is clean.
- Geolocation dataset contains a high number of duplicate records.
- No missing values found in either dataset.

Key Learning:
- Data profiling starts with understanding structure, quality and uniqueness.
- Duplicate records should be investigated before removal.

---

## Day 3 - Orders Dataset Analysis

Tasks Completed:
- Profiled Orders dataset
- Investigated null values
- Analyzed order status distribution for null records

Key Findings:

Null Values:
- order_approved_at: 160
- order_delivered_carrier_date: 1,783
- order_delivered_customer_date: 2,965

Observations:
- Most null values represent valid business scenarios.
- Missing timestamps are largely associated with cancelled, unavailable, processing and shipped orders.
- A small number of delivered orders contain missing timestamps and require further investigation.

Key Learning:
- Not all null values indicate poor data quality.
- Business context must be understood before cleaning data.

---

## Day 4 - Order Items and Payments Dataset Analysis

Tasks Completed:
- Profiled Order Items dataset
- Profiled Payments dataset
- Investigated payment behavior
- Identified dataset relationships

Order Items Findings:
- Rows: 112,650
- Null Values: 0
- Duplicate Records: 0
- Dataset is clean.
- Each record represents a product within an order.

Payments Findings:
- Rows: 103,886
- Null Values: 0
- Duplicate Records: 0
- Credit card is the dominant payment method.
- One order can have multiple payment transactions.

Business Observations:
- Installment count ranges from 0 to 24.
- Payment values range from 0 to 13,664.08.
- Some records contain payment_type = 'not_defined'.
- Some records contain 0 installments and 0 payment value requiring future investigation.

Key Learning:
- Clean datasets can still provide important business insights.
- Understanding relationships between datasets is critical for ETL design.

---

## Day 5 - Reviews Dataset Analysis

Tasks Completed:
- Profiled Reviews dataset
- Investigated review score distribution
- Analyzed missing review comments

Key Findings:
- Rows: 99,224
- Duplicate Records: 0
- review_comment_title nulls: 87,656
- review_comment_message nulls: 58,247

Business Observations:
- Majority of reviews are 5-star ratings.
- Average review score is 4.09.
- Many customers provide ratings without comments.
- Review comments appear to be optional.

Key Learning:
- Missing values in optional fields are often valid business scenarios.
- Customer satisfaction can still be analyzed even without written comments.

---

## Day 6 - Products Dataset Analysis

Tasks Completed:
- Profiled Products dataset
- Investigated missing metadata
- Investigated missing dimensional attributes

Key Findings:
- Rows: 32,951
- Duplicate Records: 0

Metadata Null Values:
- product_category_name: 610
- product_name_lenght: 610
- product_description_lenght: 610
- product_photos_qty: 610

Dimension Null Values:
- product_weight_g: 2
- product_length_cm: 2
- product_height_cm: 2
- product_width_cm: 2

Business Observations:
- 610 products are missing metadata information.
- Most of these products still contain dimensional information.
- 2 products contain missing dimensions.
- Missing values are concentrated in specific product records.

Key Learning:
- Missing values may occur in groups and indicate source-system issues.
- Product metadata is important for downstream reporting and analytics.

---

## Day 7 - Sellers and Product Category Translation Analysis

Tasks Completed:
- Profiled Sellers dataset
- Validated seller_id uniqueness
- Profiled Product Category Translation dataset

Sellers Findings:
- Rows: 3,095
- Null Values: 0
- Duplicate Records: 0
- seller_id is unique and can be treated as the primary key.

Product Category Translation Findings:
- Rows: 71
- Null Values: 0
- Duplicate Records: 0
- One-to-one mapping between Portuguese and English category names.

Key Learning:
- Unique value validation is useful for identifying primary keys.
- Lookup tables play an important role in data enrichment.

---

## Milestone 1 - Data Profiling Completed ✅

Datasets Profiled:
- Customers
- Geolocation
- Orders
- Order Items
- Payments
- Reviews
- Products
- Sellers
- Product Category Translation

Major Findings:
- Geolocation contains duplicate records.
- Orders contain business-valid null values.
- Products contain missing metadata.
- Payments support multi-payment transactions.
- Reviews contain optional text fields.

Outcome:
- Source systems understood.
- Data quality issues identified.
- Business rules documented.
- Relationships between datasets identified.

Ready For:
- Transformation Planning
- Fact and Dimension Design
- Data Cleaning Rules
- PostgreSQL Loading Phase


## Day 8 - Transformation Planning

Tasks Completed:
- Designed ETL target structure
- Identified Fact and Dimension tables
- Validated relationships between source datasets
- Created transformation plan

Fact Table:
- fact_sales

Dimension Tables:
- dim_customer
- dim_product
- dim_seller
- dim_date

Relationship Validation:

Orders:
- 99,441 unique orders

Order Items:
- 98,666 unique orders

Payments:
- 99,440 unique orders

Observations:
- 775 orders do not exist in Order Items.
- Most missing orders are unavailable or cancelled.
- Only 1 order does not have a payment record.

Key Learning:
- Always validate relationships before performing joins.
- INNER JOIN operations can remove records if matching keys are unavailable.

Outcome:
- Source-to-target mapping completed.
- Ready to begin ETL transformations.


