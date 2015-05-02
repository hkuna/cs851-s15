'''
Created on Apr 2, 2015

@author: hkuna
'''
from __future__ import print_function
import glob
import os
f = open('finaltextfileA4.txt','w')
i=0
for file in os.listdir("C:\\cs751\\cs751-assignment4\\q1-A4"):
    if file.endswith(".py"):
        print(file)
    elif file.endswith(".html"):
        print (file)
    else:
        eachfile= open(file,'r+')
        for line in eachfile:
            f.write(line + '\n')
            print (file)
            print (i)
            i = i+1
