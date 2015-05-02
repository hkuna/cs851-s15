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
import justext
f = open('1.json','r+')

completefile= f.read()
#for completefile in f:

data = json.loads(completefile)
i=0
for i in range(len(data['mementos']['list'])):
    try:
        page = urllib2.urlopen(data['mementos']['list'][i]['uri']).read()
        s= data['mementos']['list'][i]['datetime'][0:10]
        paragraphs = justext.justext(page, justext.get_stoplist('English'))
        for paragraph in paragraphs:
            if not paragraph.is_boilerplate:
                filename = '1json'+str(s)
                outputfile = open(filename, 'w')
                outputfile.write(paragraph.text.encode('utf-8') + '\n')
                i=i+1
    except Exception as e:
        print e
        continue
#print data['mementos']['list'][i]['uri']