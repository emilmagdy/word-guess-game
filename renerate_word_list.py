import random

word_list=[]

with open("word_list.txt", "r") as f:
    source_word_list = f.readlines()

for word in source_word_list:
    word = word.strip()
    if len(word) == 5:
        word_list.append(word)







