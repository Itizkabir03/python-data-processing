import pandas as pd

'''
           READING THE JSON FILE
'''

json_file = pd.read_json('Python data processing\input.json')

print(json_file)


'''
            READING SPECIFIC COLUMNS AND ROWS { SAME AS CSV METHOD }
'''

print(json_file.loc[[1,3,5],['Salary','Name']]) # captialize first  letter of 

'''
            READING JSON FILE AS RECORD
'''

xlsx_file = pd.read_json('Python data processing\example_XLSX_50.xlsx')

print(xlsx_file.to_json(orient='records', lines=True))