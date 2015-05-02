import json
import string
import subprocess
import time
import os

f = open('final20links.txt','r+')
i=1
for line in f:
	link = str(i)+"himtim" + '.json'
	subprocess.Popen(['wget','--output-document',link,"http://labs.mementoweb.org/timemap/json/"+str(line)])
	os.system('wget --output-document ' + link + " http://labs.mementoweb.org/timemap/json/"+str(line))
	i=i+1
