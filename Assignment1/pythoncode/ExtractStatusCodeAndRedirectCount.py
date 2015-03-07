'''
Created on Feb 10, 2015

@author: hkuna
'''


import json


opfile=open("responseAfterCurlCalls.txt",'r')
allstatuscodes={}
StatusCodeFile = open('statusCodeList.txt', 'w')
RedirectCount = open ('redirectCountList.txt','w')

for line in opfile:
    eachLink=json.loads(line)
    try:
        for status in eachLink["statuscodes"]:
            StatusCodeFile.write(str(status)+ '\n')
            print  str(status)
        statuslen = len(eachLink["statuscodes"])-1
        RedirectCount.write(str(statuslen)+'\n')
        print str(statuslen)
    except:    # This is the correct syntax
        continue