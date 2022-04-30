import requests
from bs4 import BeautifulSoup

'''
            FETCH THE HTML FILE
'''

url = "https://eitozx.herokuapp.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

sttrhtm = soup.prettify()

'''
            FIRST OF ALL WE WILL PRINT FEW WORDS JUST FOR DEMO
'''

print(sttrhtm[:255])


'''
            NOW WE WILL PRINT SOME ELEMENTS
'''

print(soup.title.string)
print(soup.b.string)


'''
            PRINT ALL ELEMENT
'''

for x in soup.find_all('script'): print(x)