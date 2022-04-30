from pickletools import read_bytes4
from sqlalchemy import create_engine as cg, false
import pandas as pd

'''
             READING CSV FILE
'''
csv_file = pd.read_csv('input.csv')
csv_file2 = csv_file.to_string()
'''
             CREATING ENGINE 
'''
engine = cg('sqlite:///:memory:')

'''
             STORING DATAFRAME AS DATABASE
'''
csv_file.to_sql('Data_Table', engine, index=False)

'''
             QUERY #1
'''

res1 = pd.read_sql_query('SELECT * FROM Data_Table', engine)
# print(res1)

'''
             QUERY #2 ( SELECT SPECIFIC COLUMNS )           
'''

res2 = pd.read_sql_query('SELECT name, salary FROM Data_Table', engine)
# print(res2)

# print(res2.head(2)) # You can also use pandas functions with it

'''
               QUERY #3 ( SELECT FROM SPECIFIC ROWS AND COLUMNS)
'''

res3 = pd.read_sql_query("SELECT name, salary, dept FROM Data_Table WHERE dept = 'IT'", engine)
# print(res3)


from pandas.io import sql # import sql from pandas.io

'''
               INSERTING DATA INTO RELATIONAL TABLE
'''


sql.execute("INSERT INTO Data_Table VALUES(?,?,?,?,?)", engine, params=[(9, 'Shiva', 6500.00, '2022-04-24', 'IT')])

res4 = pd.read_sql_query('SELECT * FROM Data_Table', engine)
print(res4)


'''
               DELETING DATA FROM RELATIONAL TABLE
'''

sql.execute("DELETE FROM Data_Table WHERE name = 'Dan'", engine)
res5 = pd.read_sql_query('SELECT * FROM Data_Table', engine)
print(res5)