'''
Created on Apr 1, 2015

@author: hkuna
'''


'''
Created on May 1, 2015

@author: hkuna
'''

import urllib2
import json
import os


timemapsDir = '/home/hkuna/Assignment4/timemaps'
outputfile = open('timemapCount', 'w')
filesList = os.listdir(timemapsDir)
filename = 'timemapCount'
i=0
j=0
outputfile = open(filename, 'w')
for item in filesList:
    path1 = timemapsDir+'/'+item
    with open(path1,'r') as f:
        lines = len(f.readlines())
	print lines
    outputfile.write(str(lines-3)+ '\n')
#print data['mementos']['list'][i]['uri']