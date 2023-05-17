import pandas as pd

dataframe = pd.read_csv('D:\\Study\\2022_2\\Machine Learning\Project\\all_car_adverts.csv')
num_rows = len(dataframe)

random_seed = 42
df_shuffled = dataframe.sample(frac=1, random_state=random_seed)

df_half = df_shuffled.iloc[:num_rows//2]
df_half = df_half.drop(columns=df_half.columns[0])

import pandas as pd

# Load the data into a DataFrame `df`

# Specify the column containing the numerical data
numerical_column = 'year'

# Convert the values in the numerical column to numeric values
df_half[numerical_column] = pd.to_numeric(df_half[numerical_column], errors='coerce')

# Create a Boolean mask to select rows that have non-numerical data
mask = pd.isna(df_half[numerical_column])

# Drop the rows that have non-numerical data in the numerical column
df_half = df_half[~mask]
df_half = df_half.drop(columns='car_specs')


output_file = 'D:\\Study\\2022_2\\Machine Learning\Project\\output_file.csv'
df_half.to_csv(output_file, index=False)