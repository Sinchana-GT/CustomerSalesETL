## Day 11 - PostgreSQL Load

Tasks Completed:
- Created Neon PostgreSQL database
- Connected Python to Neon
- Loaded fact_sales.csv into PostgreSQL
- Created fact_sales table

Load Result: 
fact_sales

Rows:
- 117,601

Columns:
- 35

Outcome:
- ETL pipeline completed successfully.
- Dataset available for SQL analysis.

## SQL Analysis - Payment Analysis

Query:
Revenue and Orders by Payment Type

Findings:

1. Credit Card
   - Orders: 75,991
   - Revenue: 12.72 Million
   - Primary payment method.

2. Boleto
   - Orders: 19,614
   - Revenue: 2.84 Million
   - Second most popular option.

3. Voucher
   - Orders: 3,766
   - Revenue: 785K

4. Debit Card
   - Orders: 1,521
   - Revenue: 215K

Conclusion:

Credit card payments dominate both order volume and revenue generation.

## SQL Analysis - Product Revenue Analysis

Query:
Top 10 Product Categories by Revenue

Key Findings:

1. Health & Beauty
   - Revenue: 1.49 Million

2. Watches & Gifts
   - Revenue: 1.36 Million

3. Bed Bath Table
   - Revenue: 1.31 Million

4. Sports & Leisure
   - Revenue: 1.20 Million

5. Computers Accessories
   - Revenue: 1.10 Million

Business Insight:

- Health & Beauty is the highest revenue generating category.
- Home and lifestyle products contribute significantly to revenue.
- Technology-related products are among the top performers.

## SQL Analysis - Geographic Revenue

Query:
Top States by Revenue

Findings:

1. SP
   Revenue: 6.20 Million

2. RJ
   Revenue: 2.24 Million

3. MG
   Revenue: 1.92 Million

Business Insights:

- São Paulo is the highest revenue generating state.
- The Southeast region dominates overall sales.
- Revenue is concentrated in a small number of states.
- Southern states represent strong secondary markets.

## SQL Analysis - Monthly Revenue Trend

Query:
Revenue by Month

Findings:

- Revenue increased significantly throughout 2017.
- November 2017 generated the highest revenue in 2017.
- Revenue exceeded 1 Million per month in 2018.
- March 2018 was the highest revenue month.
- September 2018 is a partial month and should not be used for trend analysis.

Business Insights:

- The marketplace experienced rapid growth.
- Revenue became stable above 1 Million per month in 2018.
- Strong seasonal spikes are visible during November.

## SQL Analysis - Customer Distribution

Query:
Top States by Customer Count

Findings:

1. SP
   Customers: 41,374

2. RJ
   Customers: 12,762

3. MG
   Customers: 11,544

Business Insights:

- São Paulo has the largest customer base.
- Customer concentration closely aligns with revenue concentration.
- Southeast region dominates both revenue and customer volume.

## SQL Analysis - Customer Retention

Query:
Average Orders Per Customer

Results:

- Unique Customers: 95,419
- Average Orders Per Customer: 1.03

Business Insight:

- Most customers placed only one order.
- Repeat purchase behavior appears limited.
- Customer retention may be an area for business improvement.

## SQL Analysis - Repeat Customer Analysis

Query:
Orders Per Customer Distribution

Results:

1 Order:
- 92,506 customers

2 Orders:
- 2,673 customers

3 Orders:
- 192 customers

4 Orders:
- 29 customers

Business Insights:

- Approximately 97% of customers made only one purchase.
- Approximately 3% of customers placed more than one order.
- Customer retention appears low.
- Opportunity exists to improve repeat purchases through loyalty and retention strategies.


## SQL Analysis Summary

KPIs Generated:

- Total Revenue: 16,566,543.85
- Total Orders: 98,665
- Total Customers: 95,419
- Total Sellers: 3,095

Payment Analysis:

- Top Payment Method: Credit Card

Product Analysis:

- Top Revenue Category: Health & Beauty

Geography Analysis:

- Top Revenue State: SP
- Top Customer State: SP

Customer Analysis:

- Average Orders Per Customer: 1.03
- Repeat Customer Rate: ~3%

Outputs Created:

- fact_sales.csv
- kpi_summary.csv

Outcome:

Business KPIs successfully generated from PostgreSQL and exported for reporting.