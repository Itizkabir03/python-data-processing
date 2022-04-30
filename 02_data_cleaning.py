import numpy as np
import pandas as pd

'''
                CREATING A DATAFRAME WITH NULL VALUES
'''

df = pd.DataFrame(np.random.randn(5, 3), index=['a','b','e','f','h'], columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df)

print(df['one'].isnull())

'''
                  FILLING NULL DATA IN DATAFRAME
'''
print(df.fillna(0))

print(df.fillna(method='pad'))

'''
                  DELETING THE NULL VALUE
'''

print(df.dropna())

'''
                     REPLACING GENERIC OR MISSING VALUE
'''

df2 = pd.DataFrame({
   'one':[10, 20, 30, 40, 50, 2000],
   'two':[1000,0, 30, 40, 50, 60]
})


print(df2.replace({1000:10, 2000:60}))