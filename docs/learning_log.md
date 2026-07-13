# Learning Log

## Pandas Concepts Learned

### read_csv()

Purpose:
Reads CSV files into a DataFrame.

Example:

pd.read_csv("file.csv")

---

### head()

Purpose:
Returns first 5 rows.

Example:

df.head()

---

### tail()

Purpose:
Returns last 5 rows.

Example:

df.tail()

---

### shape

Purpose:
Returns number of rows and columns.

Example:

df.shape

Output:

(rows, columns)

---

### columns

Purpose:
Returns column names.

Example:

df.columns

---

### info()

Purpose:
Displays:
- Data Types
- Null Counts
- Memory Usage

Example:

df.info()

---

### describe()

Purpose:
Generates statistical summary.

Example:

df.describe()

---

### isnull().sum()

Purpose:
Counts missing values.

Example:

df.isnull().sum()

---

### duplicated().sum()

Purpose:
Counts duplicate rows.

Example:

df.duplicated().sum()

---

### nunique()

Purpose:
Returns unique values count.

Example:

df.nunique()


### value_counts()

Used to understand business distribution.

Example:

data["payment_type"].value_counts()

Learning:
- Helps identify dominant categories.
- Useful for customer behavior analysis.

### describe()

Used for numerical analysis.

Learning:
- 25% = First Quartile
- 50% = Median
- 75% = Third Quartile

### Business Profiling

A dataset can be technically clean and still require analysis.

Examples:
- Payment methods
- Installment patterns
- Transaction values

Data profiling should answer:
1. Is the data clean?
2. What business patterns exist?
3. Are there unusual values?

### Primary Key Validation

To validate whether a column can act as a primary key:

data["seller_id"].nunique()
len(data)
`