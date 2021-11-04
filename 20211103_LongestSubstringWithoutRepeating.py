# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:23:18 2021

@author: alexd
"""

"""Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters."""

class Solution:
  def lengthOfLongestSubstring(self, s): 
    # Fill this in.
    long = 0
    string = ""
    lista = []
    for i, char in enumerate(s):
        string = string + char
        for letra in s[i+1:]:
            if letra == char or letra in string:
                lista.append(string)
                long = 0
                string = ""
                break
            long +=1
            string = string + letra
        
    return len(max(lista, key=len))

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
print(Solution().lengthOfLongestSubstring('geeksforgeeks'))
# 7

