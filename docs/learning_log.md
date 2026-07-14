# Learning Log

## read_csv()

Syntax:

```python
pd.read_csv("file.csv")
```

Explanation:

- Reads a CSV file into a DataFrame.
- Used to load datasets into Pandas.

---

## head()

Syntax:

```python
df.head()
```

Explanation:

- Displays the first 5 rows.
- Useful for quickly inspecting data.

---

## shape

Syntax:

```python
df.shape
```

Explanation:

- Returns the number of rows and columns.
- Output format:

```text
(rows, columns)
```

---

## columns

Syntax:

```python
df.columns
```

Explanation:

- Displays all column names.

---

## info()

Syntax:

```python
df.info()
```

Explanation:

Displays:

- Column names
- Data types
- Non-null counts
- Memory usage

---

## describe()

Syntax:

```python
df.describe()
```

Explanation:

Provides summary statistics for numeric columns.

Shows:

- Count
- Mean
- Standard Deviation
- Minimum
- Maximum
- Quartiles

---

## isnull()

Syntax:

```python
df.isnull()
```

Explanation:

- Checks for missing values.
- Returns True for null values.

---

## isnull().sum()

Syntax:

```python
df.isnull().sum()
```

Explanation:

- Counts null values in each column.

---

## duplicated()

Syntax:

```python
df.duplicated()
```

Explanation:

- Checks for duplicate rows.
- Returns True for duplicates.

---

## duplicated().sum()

Syntax:

```python
df.duplicated().sum()
```

Explanation:

- Counts duplicate rows.

---

## value_counts()

Syntax:

```python
df["column_name"].value_counts()
```

Explanation:

- Counts occurrences of unique values.
- Useful for category analysis.

---

## nunique()

Syntax:

```python
df["column_name"].nunique()
```

Explanation:

- Counts unique values.
- Useful for primary key validation.

---

## Selecting a Column

Syntax:

```python
df["column_name"]
```

Explanation:

- Selects a single column.

---

## Selecting Multiple Columns

Syntax:

```python
df[
    ["column1", "column2"]
]
```

Explanation:

- Selects multiple columns.

---

## Filtering Rows

Syntax:

```python
df[
    df["column_name"] == value
]
```

Explanation:

- Filters rows based on a condition.

Example:

```python
df[
    df["order_status"] == "canceled"
]
```

---

## Boolean Indexing

Syntax:

```python
df[condition]
```

Explanation:

- Returns rows where the condition is True.

---

## isin()

Syntax:

```python
df["column1"].isin(
    df2["column2"]
)
```

Explanation:

- Checks whether values exist in another column.
- Useful for relationship validation.

Equivalent SQL:

```sql
IN
```

---

## NOT isin()

Syntax:

```python
~df["column1"].isin(
    df2["column2"]
)
```

Explanation:

- Returns values that do not exist in another column.

Equivalent SQL:

```sql
NOT IN
```

---

## merge()

Syntax:

```python
df1.merge(
    df2,
    on="column_name",
    how="inner"
)
```

Explanation:

- Combines two DataFrames using a common column.
- Similar to SQL JOIN.

---

## on

Syntax:

```python
on="column_name"
```

Explanation:

- Specifies the common column used for joining.

Example:

```python
on="order_id"
```

---

## Inner Join

Syntax:

```python
df1.merge(
    df2,
    on="id",
    how="inner"
)
```

Explanation:

- Keeps only matching records from both datasets.

---

## Left Join

Syntax:

```python
df1.merge(
    df2,
    on="id",
    how="left"
)
```

Explanation:

- Keeps all records from the left dataset.
- Missing matches become null values.

---

## Right Join

Syntax:

```python
df1.merge(
    df2,
    on="id",
    how="right"
)
```

Explanation:

- Keeps all records from the right dataset.
- Missing matches become null values.

---

## Outer Join

Syntax:

```python
df1.merge(
    df2,
    on="id",
    how="outer"
)
```

Explanation:

- Keeps all records from both datasets.
- Missing matches become null values.

---

## tolist()

Syntax:

```python
df.columns.tolist()
```

Explanation:

- Converts values into a Python list.

---

## Creating a New Column

Syntax:

```python
df["new_column"] = (
    df["column1"]
    + df["column2"]
)
```

Example:

```python
sales_v2["total_item_value"] = (
    sales_v2["price"]
    + sales_v2["freight_value"]
)
```

Explanation:

- Creates a derived column from existing columns.

---

## Relationship Validation

Syntax:

```python
df["column_name"].nunique()
```

Explanation:

- Used to compare unique keys between datasets.
- Helps identify missing relationships before merges.

---

## Checking Columns With Null Values

Syntax:

```python
null_counts = df.isnull().sum()

print(
    null_counts[
        null_counts > 0
    ]
)
```

Explanation:

- Displays only columns that contain null values.

---

## describe() On Derived Columns

Syntax:

```python
df["column_name"].describe()
```

Example:

```python
sales_v2["total_item_value"].describe()
```

Explanation:

Used