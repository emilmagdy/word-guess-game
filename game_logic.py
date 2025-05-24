import random
import nltk
nltk.download("words")
from nltk.corpus import words

word_list=[]
for word in words.words():
    if len(word) == 5:
        word_list.append(word)






