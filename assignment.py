import pandas as pd

# loading the dataset 
trestle = pd.read_csv('trestle_academy_dataset.csv')

print(trestle.head())

# identifying missing values 
print(trestle.isnull())

# dropping missing values 
trestle.dropna(inplace=True)

# Standardize Data Types
trestle['age'] = trestle['age'].astype(int)
trestle['enrollment_date'] = pd.to_datetime(trestle['enrollment_date']).dt.date

# Normalize Text Data
trestle['name'] = trestle['name'].str.lower()
trestle['course'] = trestle['course'].str.lower()

# Filter Unwanted Data
trestle = trestle[(trestle['age'] >= 18) & (trestle['age'] <= 45)]

# Correct Inconsistent Entries
trestle['is_intern'] = trestle['is_intern'].replace({'yes': 'Yes', 'no': 'No'})
trestle['gender'] = trestle['gender'].replace({'Female':'F','Male':'M'})

print(trestle.head())

trestle.to_csv('trestle_cleaned.csv', index=False)
