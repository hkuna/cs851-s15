'''
Created on Apr 1, 2015

@author: hkuna
'''
'''
Created on Apr 1, 2015

@author: hkuna
'''


import urllib2
import json
import justext
f = open('urlStatusAfterCurlCalls7','r+')
i=1000
for line in f:
    try:
        data = json.loads(line)
        page = urllib2.urlopen(data['lasturl']).read()
        paragraphs = justext.justext(page, justext.get_stoplist('English'))
        
        i=i+1
        for paragraph in paragraphs:
            if not paragraph.is_boilerplate:
                filename = 'textfromhtml8'+str(i)
                outputfile = open(filename, 'w')
                outputfile.write(paragraph.text.encode('utf-8') + '\n')
    except Exception as e:
        print data['lasturl']
        continue
