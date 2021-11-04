# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:13:55 2021

@author: alexd
"""

# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def solution(sentence):
    #Complete code here
    for mark in ",.?!-+_":
        sentence.replace(mark,'')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)

print(solution(sentence1))
print(solution(sentence2))

#Solution:
#    Output:
#       4.2
#       4.08

"""El truco estaba en reemplazar los caracteres raros y saber que los strings son modificables.

"""