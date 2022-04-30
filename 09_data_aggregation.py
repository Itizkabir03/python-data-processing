import pandas as pd
from numpy.random import randn

'''
            AGGREGATION WORKS ONLY NUMERIC TYPES COLUMN
'''

df = pd.read_csv('nba.csv')

# prints top 10 data of file

print(df.head(10))


print(df.aggregate(['sum', 'min']))


'''
            AGGREGATION ON SPECIFIC COLUMNS
'''

print(df.aggregate({'Number':['min', 'max'], 'Age' :['min', 'max'], 'Weight' :['min', 'max']}))