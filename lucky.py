#!python
#lucky.py - opens serveral google search results.
import bs4,webbrowser,requests,sys
print('baiduing...')
res=requests.get('http://www.baidu.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()
#TODO: retrieve top search result links.

#TODO: open a browser tab for each result.