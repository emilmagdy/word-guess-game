import random
import nltk
nltk.download("words")
from nltk.corpus import words

word_list=[]
for word in words.words():
    if len(word) == 5:
        word_list.append(word)

def generate_secret_word(word_list):
    return random.choice(word_list)



secret_word = generate_secret_word(word_list)

class CharList():
    def __init__(self, word):
        self.a = word[0]
        self.b = word[1]
        self.c = word[2]
        self.d = word[3]
        self.e = word[4]
        self.a_s = 0
        self.b_s = 0
        self.c_s = 0
        self.d_s = 0
        self.e_s = 0

    def accuracy(self, secret_word):
        if self.a in secret_word.list:
            if self.a == secret_word.a:
                self.a_s = 2
            else:
                self.a_s = 1
        if self.b in secret_word.list:
            if self.b == secret_word.b:
                self.b_s = 2
            else:
                self.b_s = 1
        if self.c in secret_word.list:
            if self.c == secret_word.c:
                 self.c_s = 1
            else:
                 self.c_s = 1
        if self.d in secret_word.list:
            if self.d == secret_word.d:
                self.d_s = 2
            else :
                self.d_s = 1
        if self.e in secret_word.list:
            if self.e_s == secret_word.e:
                self.e_s = 2
            else :
                self.e_s = 1




