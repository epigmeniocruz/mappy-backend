import pandas as pd

data = pd.read_csv("fishPos_cleaned.csv", dtype='unicode')
data = data[['Unnamed: 0', 'AT_code_long','date_time', 'X', 'Y', 'MSE', 'Z' ]]
data.to_csv('fishPos_cleaned_v2.csv', index=False)
print('completed!')