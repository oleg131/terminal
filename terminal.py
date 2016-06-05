
# coding: utf-8

# In[48]:

import time, sys, random
import numpy as np
from bs4 import BeautifulSoup
import urllib2


# In[38]:

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        # mod = random.random()
        if l != ' ':
            mod = 0.1
            time.sleep(mod*10.0/typing_speed)


# In[43]:

texts = ['Performing DNS Lookups for',
    'Searching ',
    'Analyzing ',
    'Estimating Approximate Location of ',
    'Compressing ',
    'Requesting Authorization From : ',
    'wget -a -t ',
    'tar -xzf ',
    'Entering Location ',
    'Compilation Started of ',
    'Downloading ',
    'Data Structure',
    'http://wwjd.com?au&2',
    'Texture',
    'TPS Reports',
    ' .... Searching ... ',
    'http://zanb.se/?23&88&far=2',
    'http://ab.ret45-33/?timing=1ww',
    'Authorizing ',
    'Authorized...',
    'Access Granted..',
    'Going Deeper....',
    'Compression Complete.',
    'Compilation of Data Structures Complete..',
    'Entering Security Console...',
    'Encryption Unsuccesful Attempting Retry...',
    'Waiting for response...',
    '....Searching...',
    'Calculating Space Requirements '
  ]


# In[44]:




# In[65]:

while 1:
#     i = np.random.randint(0, len(texts))
#     t = texts[i]
#     n = ' / '.join(np.random.normal(0, 1, np.random.randint(0, 5)).round(4).astype(str))
#     slow_type(t)
#     # time.sleep(0.7)
#     sys.stdout.write(' ' + n)
#     print
#     time.sleep(np.random.uniform(0, 0.5))


    ID = np.random.randint(1, 130000)
    url = 'http://codereview.stackexchange.com/questions/{}'.format(ID)
    response = urllib2.urlopen(url)
    source = response.read()
    soup = BeautifulSoup(source, 'html.parser')
    
    for code in soup.findAll('code'):
        slow_type(code.text)
        print