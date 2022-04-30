import pandas as pd

'''
            MERGING DATA
'''


left = pd.DataFrame({
   'ID': [1,2,3,4,5],
   'Name': ["Uday", "Diya", "Prashant", "Shudhanshu", "rahul"],
   'Usercode': ["UC1", "UC-2", "UC-3", "UC-4", "UC-5"] 
})



right = pd.DataFrame({
   'ID': [1,2,3,4,5],
   'Name': ["Sano", "Astro", "Sammie", "Soumya", "Yash"],
   'Usercode': ["UC-6", "UC-7", "UC-8", "UC-9", "UC-10"] 
})




'''
            GROUPING DATA
'''

players_data = pd.DataFrame({
   'Name': ['Prashant', 'Prashant', 'Uday', 'Uday', 'Uday', 'Shudhanshu', 'Atharv', 'Rahul', 'Rahul', 'Rahul', 'Chirag', 'Yash'],
   'Rank': [2,1,2,3,5,7,1,4,3,3,3,4],
   'Year': [2014, 2015,2015, 2017, 2018, 2011, 2012, 2014, 2015, 2021, 2021, 2016]
})

grouped = players_data.groupby('Year')

print(grouped.get_group(2015))


'''
            CONCATENATING DATA
'''

print(pd.concat([left, right]))