# Q1 : Create the dataset 
import pandas as pd
data = {
    'Tid': [1, 2, 3, 4, 5,6,7,8,9,10],
    'Refund':['Yes','No','No','Yes','No','No','Yes','No','No','No'],
    'MaritalStatus':['Single','Married','Single','Married','Divorced','Married','Divorced','Single','Married','Single'],
    'TaxableIncome':['125K','100K','70K','120K','95K','60K','220K','85K','75K','90K'],
    'Cheat':['No','No','No','No','Yes','No','No','Yes','No','Yes']
}
df = pd.DataFrame(data)
print(df)

#Q2: Locate row 0, 4, 7, 8 using DataFrame 
print(df.loc[[0,4,7,8]])

#Q3: Do following tasks 
# (i) Select rows from index 3 to 7 
print(df.loc[3:7])
#(ii) Select rows from index 4 to 8 and column 2 to 4 
print(df.iloc[4:9, 2:5])
#(iii) Select all rows with column index 1 to 3 
print(df.iloc[:, 1:4])

#Q4: Read a csv file and display the first 5 rows 
df = pd.read_csv('Assignment_3\Iris.csv')
print(df.head())

#Q5: Delete row 4 and column 3 and display result 
df.drop(index=3, inplace=True)
df.drop(columns=df.columns[3], inplace=True)
print(df.head(10))

#Q6: Create a csv file employees.csv and do following operations
df = pd.read_csv('Assignment_3\employees.csv')
print(df.head())
#a. Shape of dataframe
print("Shape:", df.shape)
#b. Summary of dataframe
print("Summary:",df.info())
#c. Generate descriptive statistics
print("Descriptive Statistics:", df.describe())
#d. Display first 5 rows and last 3 rows
print("First 5 rows:",df.head())
print("Last 3 rows:",df.tail(3))

#e. Calculate following statistics : i. average salary, ii. total bonus, iii. youngest employee's age, iv. highest performance rating
print("Average Salary:", df['Salary'].mean())
print("Total Bonus:", df['Bonus'].sum())
print("Youngest Employee's Age:", df['Age'].min())
print("Highest Performance Rating:", df['Rating'].max())

#f. Sort by salary column in descending order 
df_sorted = df.sort_values(by='Salary', ascending=False)
print(df_sorted)

#g. Add a new column that categorizes employees based on their rating 
def performance_category(rating):
    if rating >= 4.5:
        return 'Excellent'
    elif rating >= 4.0:
        return 'Good'
    else: 
        return 'Average'

df['Performance'] = df['Rating'].apply(performance_category)
print(df)

#h. Identify missing values in dataframe
print(df.isnull().sum())
print("As sum for each column = 0, there is no NULL values")

#i. Rename Employee_ID to ID
df.rename(columns={'Employee_ID': 'ID'}, inplace=True)
print(df)

#j. Find employees who have more than 5 years of experience and belong to IT department
filtered_df = df[(df['Years_of_Experience'] > 5) & (df['Department'] == 'IT')]
print("Employees with more than 5 years of experience in IT department:")
print(filtered_df)

#k. Modify by adding new column , Tax, which deducts 10% of salary 
df['Tax'] = df['Salary'] * 0.1
print(df)

#l. save modified dataframe to a new csv file 
df.to_csv('Assignment_3\modified_employees.csv', index=False)
