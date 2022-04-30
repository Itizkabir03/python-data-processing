# Data operation in numpy and pandas
from random import Random
import numpy as np
import pandas as pd


df1 = np.array(['a', 'b', 'c', 'd', 'e'])

pd1 = pd.Series(df1)

print(pd1)

df2 = {
   'Name':['Eito', 'Uday', 'Nohty', 'Astro', 'Soumya', 'Diya'],
   'Work': ['Python Developer', 'Web developer', 'Lode ka developer', 'Bas Nam Ka Developer', 'Economics Wali ladki', 'Bencho hai hi ni developer']
}

pd2 = pd.DataFrame(df2)

print(pd2)

pd3 = pd.DataFrame(df2, index=['Landi_1', 'Landi_2', 'Landi_3', 'Landi_4', 'Landi_5', 'Landi_6'])

print(pd3)
