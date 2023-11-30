import pandas as pd

d = {
    'one': [1, 2, 3], 
    'two': [4, 5, 6], 
    'three': [7, 8, 9],
    'four': [10, 11, 12],
    'five': [13, 14, 15],
    'six': [16, 17, 18],
    'seven': [19, 20, 21]
}

df = pd.DataFrame(d)

print(df)

count_abrevation = df.shape[0]
count_columns = df.shape[1]

print(count_columns,count_abrevation)