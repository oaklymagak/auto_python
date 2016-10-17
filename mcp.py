#!python
#mcb.pyw - saves and loads pieces of text to the clipboard.
#usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
#  py.exe mcb.pyw <keyword> - loads keyword to clipboard.
import shelve,pyperclip,sys
mcbshelf=shelve.open('mcb')
#TODO:save clipboard content.
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbshelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
#TODO:list keywords and load content.

mcbshelf.close()