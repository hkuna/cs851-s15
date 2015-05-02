'''
Created on May 1, 2015

@author: hkuna
'''
from nltk.util import ngrams
import json
import sys
import os
import string

def jaccardDistance(list1, list2):
    union = set(list1).union(list2)
    intersect = set(list1).intersection(list2)
    dist = (len(union) - len(intersect)) * 1.0 / len(union)
    return dist
    
def wordsFromFile(filePath):
    text = ''
    print filePath
    with open(filePath, 'r') as textFile:
        for line in textFile:
            text = text + extractWords(line).strip() + ' '
    words = text.strip().split(' ')
    if '' in words:
        words.remove('')
    return words
def calculateNgrams():
    finalGrams = ngrams(sentence.split(), n)
    for grams in finalGrams:
      print grams

def extractWords(s):
    valid_characters = string.ascii_letters
    valid_following_character = "'-"
    letters = []
    for letter in s:
        if letter in valid_characters:
            letters.append(letter)
        elif len(letters) > 0 and \
            letter in valid_following_character and \
            letters[-1] in valid_characters:
            letters.append(letter)
        elif len(letters) > 0 and letters[-1] != ' ':
            letters.append(' ')
    return ''.join(letters)

mementosDir = 'C:\\cs751\\cs751-assignment4\\q3-A4\\link18'
outputfile1 = open('UnigramJackardDistance', 'w') 
filesList = os.listdir(mementosDir) 
firstItem = 1 
for item in filesList:
    if firstItem==1:
         path1 = mementosDir+'\\'+item
         words1 = wordsFromFile(path1)
         words1.sort()
    else:
        path1 = mementosDir+'\\'+item
        words2 = wordsFromFile(path1)
        words2.sort()
        jacadDistanceUni = jaccardDistance(words1,words2)
        outputfile1.write(str(jacadDistanceUni)+ '\n')
    firstItem = firstItem+1
