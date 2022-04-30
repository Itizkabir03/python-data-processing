import pandas as pd

'''
           READING THE CSV FILE
'''

csv_file = pd.read_csv('E:\data science learning\Python data processing\input.csv')

print(csv_file)

'''
           READING A SPECIFIC ROW
           SLICE RESULT FOR FIRST FIVE ROW
'''


print(csv_file[::2]['name'])  # Always enter row name in lowercase

'''
          USE MULTI AXES INDEXING FUNCTION TO ACCESS MULTIPLE COLUMNS
'''

print(csv_file.loc[:,['name','salary']])

'''
         READING SPECIFIC COLUMNS AND ROWS
'''

print(csv_file.loc[[1,3,5],['name', 'salary']])          

'''
         READING SPECIFIC COLUMNS FOR A RANGE OF ROWS
'''

print(csv_file.loc[2:6, ['name']])
