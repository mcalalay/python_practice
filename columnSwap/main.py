import pandas as pd

my_data = {'Sr.no': [1, 2, 3, 4, 5],
'Name': ['Ram', 'Sham', 'Sonu',
'Tinu', 'Monu'],
'Maths Score': [45, 67, 89, 74, 56]}
df = pd.DataFrame(data = my_data)

# printing the original DataFrame
print("My Original DataFrame")
print(df)

# altering the DataFrame
df = df[['Sr.no', 'Maths Score', 'Name']]

# printing the altered DataFrame
print('After altering Name and Maths Score')
print(df)