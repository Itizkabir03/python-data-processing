import nltk
from nltk.stem.porter import PorterStemmer

syntax = "Python is great programming language. It can be used for data science, game develoment, data visualization, web developent"
porter_stemmer = PorterStemmer()


nltk_tokens = nltk.word_tokenize(syntax)
#Next find the roots of the word
for w in nltk_tokens:
       print("Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w)))