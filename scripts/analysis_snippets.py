import pandas as pd

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

data = datasets["customers"] #change value for each analysis

# Geolocation Dataset Analysis

geo = datasets["geolocation"]

print(geo[geo.duplicated()].head())
print(geo[geo.duplicated()].shape)

print("Total Rows:", len(geo))

print("Unique Rows:", len(geo.drop_duplicates()))

print(geo.nunique())

print("Duplicate Rows:", geo.duplicated().sum())

#order dataset Analysis

null_approved =data[data["order_approved_at"].isnull()]
print(null_approved)
print(null_approved["order_status"].value_counts())

null_carrier = data[data["order_delivered_carrier_date"].isnull()]
print(null_carrier["order_status"].value_counts())

null_delivery = data[data["order_delivered_customer_date"].isnull()]
print(null_delivery["order_status"].value_counts())

#payment dataset Analysis

print(len(data))
print(data["order_id"].nunique())
print(data["payment_type"].value_counts())
print(data["payment_installments"].describe())
print(data["payment_value"].describe())

#review dataset analysis

print(data["review_score"].value_counts().sort_index()) #
print(data["review_score"].describe())
print(data[data["review_comment_message"].isnull()]["review_score"].value_counts())


#product dataset analysis

print(data[data["product_category_name"].isnull()].head())
print(data[data["product_category_name"].isnull()].shape)
print(data[data["product_weight_g"].isnull()])

#product Category name analysis

print( len(data))
print(data["product_category_name"].value_counts())
print(data["product_category_name"].nunique())


#seller data analysis

print(data["seller_id"].nunique())
print(len(data))