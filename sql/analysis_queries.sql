-- Total Revenue
SELECT
    ROUND(SUM(total_item_value), 2) AS total_revenue
FROM fact_sales;

-- Total Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM fact_sales;

-- Total Customers
SELECT
    COUNT(DISTINCT customer_id) AS total_customers
FROM fact_sales;

-- Total Sellers
SELECT
    COUNT(DISTINCT seller_id) AS total_sellers
FROM fact_sales;

---Which payment method is most used.
--Which payment method generates the most revenue.

SELECT
    payment_type,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(total_item_value)::numeric, 2) AS revenue
FROM fact_sales
GROUP BY payment_type
ORDER BY revenue DESC;

-- Top 10 Product Categories by Revenue
SELECT
    product_category_name_english,
    ROUND(SUM(total_item_value)::numeric, 2) AS revenue
FROM fact_sales
GROUP BY product_category_name_english
ORDER BY revenue DESC
LIMIT 10;

--Top 10 States by Revenue
SELECT
    customer_state,
    ROUND(SUM(total_item_value)::numeric, 2) AS revenue
FROM fact_sales
GROUP BY customer_state
ORDER BY revenue DESC
LIMIT 10;

--Monthly Revenue Trend

SELECT
    DATE_TRUNC('month', order_purchase_timestamp::timestamp) AS month,
    ROUND(SUM(total_item_value)::numeric, 2) AS revenue
FROM fact_sales
GROUP BY month
ORDER BY month;


-- state having larger customer base

SELECT
    customer_state,
    COUNT(DISTINCT customer_id) AS customers
FROM fact_sales
GROUP BY customer_state
ORDER BY customers DESC
LIMIT 10;

-- to check customers repeatness in buying

SELECT
    COUNT(*) AS total_customers,
    AVG(order_count) AS avg_orders_per_customer
FROM (
    SELECT
        customer_unique_id,
        COUNT(DISTINCT order_id) AS order_count
    FROM fact_sales
    GROUP BY customer_unique_id
) customer_orders;

-- check repeated buyers

SELECT
    order_count,
    COUNT(*) AS customers
FROM (
    SELECT
        customer_unique_id,
        COUNT(DISTINCT order_id) AS order_count
    FROM fact_sales
    GROUP BY customer_unique_id
) customer_orders
GROUP BY order_count
ORDER BY order_count;