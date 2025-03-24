import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [25, 30, 22, 35, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Salary': [50000, 55000, 40000, 70000, 48000]
}

df = pd.DataFrame(data)

# 1. Accessing and Modifying the Index
print("1. Accessing the Index:")
print(df.index)

# 2. Setting a Custom Index
print("\n2. Setting 'Name' as the Index:")
df_with_index = df.set_index('Name')
print(df_with_index)

# 3. Resetting the Index
print("\n3. Resetting the Index:")
df_reset = df.reset_index()
print(df_reset)

# 4. Indexing with loc
# Set 'Name' as index again to use loc properly
df_with_index = df.set_index('Name')
print("\n4. Indexing with loc:")
row = df_with_index.loc['Alice']
print(row)

# 5. Changing the Index
print("\n5. Changing the Index to 'Age':")
df_with_new_index = df.set_index('Age')
print(df_with_new_index)

# -----------------------------
# Pandas Access DataFrame

# Display the entire DataFrame
print("\nDisplaying the Entire DataFrame:")
print(df)

# 1. Accessing Columns From DataFrame
print("\n1. Accessing the 'Age' Column:")
age_column = df['Age']
print(age_column)

# 2. Accessing Rows by Index
print("\n2. Accessing the Row at Index 1 (Second Row):")
second_row = df.iloc[1]
print(second_row)

# 3. Accessing Multiple Rows or Columns
print("\n3. Accessing Multiple Rows and Columns:")
subset = df.loc[0:2, ['Name', 'Age']]
print(subset)

# 4. Accessing Rows Based on Conditions
print("\n4. Accessing Rows Where 'Age' is Greater Than 25:")
filtered_data = df[df['Age'] > 25]
print(filtered_data)

# 5. Accessing Specific Cells with at and iat
print("\n5. Accessing 'Salary' of the Row with Label 2:")
salary_at_index_2 = df.at[2, 'Salary']
print(salary_at_index_2)


