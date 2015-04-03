'''
Created on Apr 2, 2015

@author: hkuna
'''
from __future__ import print_function
import glob
import os
f = open('finalhtmlfile.html','w')
i=0
for file in os.listdir("C:\\Users\\systems\\workspace\\Assignment3-cs751\\src\\assign3\\allhtml\\Assignment3"):
    if file.endswith(".py"):
        print(file)
    elif file.endswith(".txt"):
        print (file)
    else:
        eachfile= open(file,'r+')
        for line in eachfile:
            f.write(line + '\n')
            print (file)
            print (i)
            i = i+1
