"""
Assignment-3
UCS420 "Cognitive Computing"
Pandas

Run this script with:  python Assignment3_Pandas.py
It expects iris.csv to be present in the same folder for Q4 and Q5
(download it from https://www.kaggle.com/datasets/uciml/iris and place
it next to this script, or use the iris.csv generated alongside this
file).
"""

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------------------
# Q.1  Create the dataset shown in the table
# ---------------------------------------------------------------------
section("Q.1 - Create the dataset")

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced",
                        "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K",
                        "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"],
}

df1 = pd.DataFrame(data)
print(df1)


# ---------------------------------------------------------------------
# Q.2  Locate rows 0, 4, 7 and 8 using the DataFrame
# ---------------------------------------------------------------------
section("Q.2 - Locate rows 0, 4, 7, 8")

rows_2 = df1.loc[[0, 4, 7, 8]]
print(rows_2)


# ---------------------------------------------------------------------
# Q.3  Navigate the DataFrame
# ---------------------------------------------------------------------
section("Q.3.1 - Select rows from index 3 to 7")
print(df1.loc[3:7])

section("Q.3.2 - Select rows from index 4 to 8, columns 2 to 4")
# iloc uses position-based indexing; columns 2 to 4 -> stop is exclusive,
# so we use 2:5 to include column index 4 ("Marital Status" .. "Cheat")
print(df1.iloc[4:9, 2:5])

section("Q.3.3 - Select all rows, columns index 1 to 3 (include index 3)")
print(df1.iloc[:, 1:4])


# ---------------------------------------------------------------------
# Q.4  Read a csv file and display its first five rows (Iris dataset)
# ---------------------------------------------------------------------
section("Q.4 - Read iris.csv and show first five rows")

iris_df = pd.read_csv("iris.csv")
print(iris_df.head())


# ---------------------------------------------------------------------
# Q.5  Delete row 4 and column 3 from the Iris dataset
# ---------------------------------------------------------------------
section("Q.5 - Delete row 4 and column index 3, display result")

iris_modified = iris_df.drop(index=4)
iris_modified = iris_modified.drop(iris_modified.columns[3], axis=1)
print(iris_modified.head())


# ---------------------------------------------------------------------
# Q.6  Employees dataset
# ---------------------------------------------------------------------
section("Q.6 - Create employees.csv")

emp_data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01",
                      "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5],
}

emp_df = pd.DataFrame(emp_data)
emp_df.to_csv("employees.csv", index=False)
print(emp_df)

# a) Shape of the DataFrame
section("Q.6.a - Shape of the DataFrame")
print(emp_df.shape)

# b) Summary: data types and non-null counts
section("Q.6.b - DataFrame info()")
emp_df.info()

# c) Descriptive statistics
section("Q.6.c - Descriptive statistics")
print(emp_df.describe())

# d) First 5 rows and last 3 rows
section("Q.6.d - First 5 rows")
print(emp_df.head())
section("Q.6.d - Last 3 rows")
print(emp_df.tail(3))

# e) Statistics
section("Q.6.e - Statistics")
avg_salary = emp_df["Salary"].mean()
total_bonus = emp_df["Bonus"].sum()
youngest_age = emp_df["Age"].min()
highest_rating = emp_df["Rating"].max()
print(f"i.   Average salary: {avg_salary}")
print(f"ii.  Total bonus paid: {total_bonus}")
print(f"iii. Youngest employee's age: {youngest_age}")
print(f"iv.  Highest performance rating: {highest_rating}")

# f) Sort by Salary descending
section("Q.6.f - Sorted by Salary (descending)")
emp_sorted = emp_df.sort_values(by="Salary", ascending=False)
print(emp_sorted)

# g) Performance category column
section("Q.6.g - Performance category column")


def categorize(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"


emp_df["Performance_Category"] = emp_df["Rating"].apply(categorize)
print(emp_df[["Name", "Rating", "Performance_Category"]])

# h) Missing values
section("Q.6.h - Missing values")
print(emp_df.isnull().sum())

# i) Rename Employee_ID to ID
section("Q.6.i - Rename Employee_ID to ID")
emp_df = emp_df.rename(columns={"Employee_ID": "ID"})
print(emp_df.columns.tolist())

# j) Filtering
section("Q.6.j.i - More than 5 years of experience")
print(emp_df[emp_df["Years_of_Experience"] > 5])

section("Q.6.j.ii - Belong to IT department")
print(emp_df[emp_df["Department"] == "IT"])

# k) Tax column (10% of Salary)
section("Q.6.k - Add Tax column (10% of Salary)")
emp_df["Tax"] = emp_df["Salary"] * 0.10
print(emp_df[["Name", "Salary", "Tax"]])

# l) Save modified DataFrame to a new CSV
section("Q.6.l - Save modified DataFrame to CSV")
emp_df.to_csv("employees_modified.csv", index=False)
print("Saved to employees_modified.csv")
