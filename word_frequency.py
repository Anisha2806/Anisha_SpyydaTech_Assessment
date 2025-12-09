import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
nltk.download('punkt_tab')
text=input("enter your text:")

tokens=word_tokenize(text)
freq=FreqDist(tokens)
for key,value in freq.items():
    print(f"{key}:{value}")
