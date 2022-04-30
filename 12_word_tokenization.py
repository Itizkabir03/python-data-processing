'''
            Word tokenization is the process of splitting a large sample of text into words. T
'''

'''
        pip install nltk
        plz download punkt after installing nltk

        step 1: open a python file
        step 2: import nltk
        step 3: nltk.download('punkt')
        step 4: run that file
'''

import nltk

syntax = "Python is great programming language. It can be used for data science, game develoment, data visualization, web developent"

p = nltk.word_tokenize(syntax)
print(p)

# access the words by index

print(p[3])