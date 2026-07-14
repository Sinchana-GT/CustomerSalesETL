# Learning Log

## read_csv()

Purpose:
Read a CSV file into a DataFrame.

Example:

```python
pd.read_csv("file.csv")
```

---

## head()

Purpose:
Display first 5 rows.

Example:

```python
df.head()
```

---

## shape

Purpose:
Get number of rows and columns.

Example:

```python
df.shape
```

Output:

```text
(rows, columns)
```

---

## columns

Purpose:
Display column names.

Example:

```python
df.columns
```

---

## info()

Purpose:
Display dataset information.

Shows:

- Data types
- Null values
- Memory usage

Example:

```python
df.info()
```

---

## describe()

Purpose:
Generate statistical summary.

Example:

```python
df.describe()
```

Learning:

- 25% = First Quartile
- 50% = Median
- 75% = Third Quartile

---

## isnull().sum()

Purpose:
Count null values.

Example:

```python
df.isnull().sum()
```

---

## duplicated().sum()

Purpose:
Count duplicate records.

Example:

```python
df.duplicated().sum()
```

---

## value_counts()

Purpose:
Count occurrences of unique values.

Example:

```python
data["payment_type"].value_counts()
```

Used For:

- Category analysis
- Business distribution analysis

---

## nunique()

Purpose:
Count unique values.

Example:

```python
data["seller_id"].nunique()
```

Used For:

- Primary key validation

---

## Filtering Rows

Purpose:
Select rows that satisfy a condition.

Example:

```python
data[
    data["order_status"] == "canceled"
]
```

---

## Boolean Indexing

Purpose:
Filter data using True/False conditions.

Example:

```python
data[
    data["review_comment_message"].isnull()
]
```

---

## isin()

Purpose:
Check whether values exist in another column.

Example:

```python
orders["order_id"].isin(
    order_items["order_id"]
)
```

Learning:

Used for relationship validation between datasets.

---

## ~ (NOT Operator)

Purpose:
Reverse a condition.

Example:

```python
~orders["order_id"].isin(
    order_items["order_id"]
)
```

Learning:

Used to find missing records.

Equivalent to SQL:

```sql
NOT IN
```

---

## merge()

Purpose:
Combine two datasets using a common key.

Example:

```python
orders.merge(
    order_items,
    on="order_id",
    how="inner"
)
```

Learning:

Similar to SQL JOIN.

---

## merge() - on

Purpose:
Specify the common column used for joining.

Example:

```python
on="order_id"
```

---

## merge() - how

Purpose:
Specify join type.

Example:

```python
how="inner"
```

Types:

```text
inner
left
right
outer
```

---

## tolist()

Purpose:
Convert values to a Python list.

Example:

```python
df.columns.tolist()
```

Used For:

Displaying column names.

---

## Creating New Columns

Purpose:
Create derived business metrics.

Example:

```python
sales_v2["total_item_value"] = (
    sales_v2["price"]
    + sales_v2["freight_value"]
)
```

Learning:

New columns can be created from existing columns.

---

## Relationship Validation

Learning:

Always validate relationships before merging datasets.

Examples:

```text
Orders → Order Items

Orders → Payments
```

Purpose:

- Identify missing records
- Understand join impact

---

## One-to-Many Relationships

Learning:

One record can have multiple related records.

Examples:

```text
One Order → Many Order Items

One Order → Many Payments
```

Impact:

- Row counts increase after merges.

---

## Business Valid Nulls

Learning:

Not all null values indicate poor data quality.

Examples:

- Cancelled orders
- Unavailable orders
- Optional review comments

Key Takeaway:

Understand business context before cleaning data.

---

## Derived Columns

Learning:

Transformations are not limited to joins.

Example:

```python
total_item_value =price + freight_value
```

Used to create business metrics.

---

## Data Validation

Purpose:
Validate transformed data.

Example:

```python
sales_v2["total_item_value"].describe()
```

Checks:

- Min
- Max
- Average
- Distribution

---

## Fact Table

Learning:

Stores business transactions