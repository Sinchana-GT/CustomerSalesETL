import pandas as pd

# Load final transformed dataset
sales_v6 = pd.read_csv("../output/fact_sales.csv")

# =====================================
# Customer Dimension
# =====================================
dim_customer = sales_v6[
    [
        "customer_id",
        "customer_unique_id",
        "customer_zip_code_prefix",
        "customer_city",
        "customer_state"
    ]
].drop_duplicates()

# =====================================
# Product Dimension
# =====================================
dim_product = sales_v6[
    [
        "product_id",
        "product_category_name",
        "product_category_name_english",
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]
].drop_duplicates()

# =====================================
# Seller Dimension
# =====================================
dim_seller = sales_v6[
    [
        "seller_id",
        "seller_zip_code_prefix",
        "seller_city",
        "seller_state"
    ]
].drop_duplicates()

# =====================================
# Fact Sales
# =====================================
fact_sales_star = sales_v6[
    [
        "order_id",
        "order_item_id",
        "customer_id",
        "product_id",
        "seller_id",
        "payment_sequential",
        "order_purchase_timestamp",
        "order_status",
        "payment_type",
        "payment_installments",
        "payment_value",
        "price",
        "freight_value",
        "total_item_value"
    ]
]

# =====================================
# Validation
# =====================================
print("\nCustomer Dimension Shape:", dim_customer.shape)
print("Customer Duplicates:", dim_customer.duplicated().sum())

print("\nProduct Dimension Shape:", dim_product.shape)
print("Product Duplicates:", dim_product.duplicated().sum())

print("\nSeller Dimension Shape:", dim_seller.shape)
print("Seller Duplicates:", dim_seller.duplicated().sum())

print("\nFact Sales Shape:", fact_sales_star.shape)

# =====================================
# Export Files
# =====================================
dim_customer.to_csv(
    "../output/dim_customer.csv",
    index=False
)

dim_product.to_csv(
    "../output/dim_product.csv",
    index=False
)

dim_seller.to_csv(
    "../output/dim_seller.csv",
    index=False
)

fact_sales_star.to_csv(
    "../output/fact_sales_star.csv",
    index=False
)

print("\nStar Schema Files Created Successfully!")

# =====================================
# Validating
# =====================================

print(dim_customer.shape)
print(dim_product.shape)
print(dim_seller.shape)
print(fact_sales_star.shape)

print(dim_customer["customer_id"].nunique(),len(dim_customer))

print(dim_product["product_id"].nunique(),len(dim_product))

print(dim_seller["seller_id"].nunique(),len(dim_seller))

print(fact_sales_star.duplicated().sum())

print(fact_sales_star[fact_sales_star.duplicated(keep=False)].head(20))
