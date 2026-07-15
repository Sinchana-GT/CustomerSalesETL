import pandas as pd
from sqlalchemy import create_engine

# Load fact sales dataset
fact_sales = pd.read_csv("../output/fact_sales.csv")

# Neon PostgreSQL connection
engine = create_engine(
    "postgresql://neondb_owner:npg_ogntx9W3Bash@ep-small-glade-attvzk99-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

# Load data into PostgreSQL
fact_sales.to_sql(
    "fact_sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully.")