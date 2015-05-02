'''
Created on Apr 30, 2015

@author: hkuna
'''
import json
import string
import subprocess
import time




uni1 = list(line.strip() for line in open('textfromhtml11050uniGram.txt'))
print len(uni1)
uni2 = list(line.strip() for line in open('textfromhtml11051uniGram.txt'))
print len(uni1)
union = set(uni1).union(uni2)
print union
print len(union)
intersect = set(uni2).intersection(uni1)
print intersect
print len(intersect)
dist = (len(union) - len(intersect)) / len(union)
print dist
            