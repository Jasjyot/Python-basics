
#stemming example

#finding the root word

#nltk= Natural Language Tool Kit

from nltk.stem.porter import *
stemmer = PorterStemmer()

print(stemmer.stem('fishing'))      #fish
print(stemmer.stem('fished'))       #fish 
print(stemmer.stem('fisher'))        #fisher
print(stemmer.stem('fishes'))       #fish
print(stemmer.stem('fishing net'))  #fishing net

