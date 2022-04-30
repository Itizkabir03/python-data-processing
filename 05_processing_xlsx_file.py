import pandas as pd

xlsx_file = pd.read_excel('Python data processing\example_XLSX_50.xlsx')

print(xlsx_file)

'''
          SELECTING A SPECIFIC ROW AND COLUMNS
'''

print(xlsx_file.loc[[1,3,5], ['First Name', 'Last Name']])

print(xlsx_file.loc[2:6, ['First Name']])