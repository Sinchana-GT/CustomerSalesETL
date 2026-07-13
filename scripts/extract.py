import pandas as pd
pd.set_option('display.max_columns', None)

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

data = datasets["product_category_name"]

print("Rows and Columns:", data.shape)
print("\nColumns:", data.columns.tolist())

print("\nInfo:")
data.info()
print("\nNull Values:",data.isnull().sum())
print("\nDuplicate Rows:",data.duplicated().sum())

#print("\nFirst 5 Rows:", data.head())
#print("\nStatistics:",data.describe())


