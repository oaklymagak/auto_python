import os
# import shelve
# a=os.path.exists('C:\\Windows')
# print a
# print os.path.isdir('C:\\Windows\\System32')
# print os.listdir('.')
# hellofile=open('.\\hello.txt','a')
# hellofile.write('hello world\nmy name is vincent\n')
# hellofile.close()
# hellofile1=open('.\\hello.txt','r')
# hellocontent=hellofile1.readlines()
# print hellocontent
# hellofile1.close()
# shelffile=shelve.open('mydata')
# cat=['zopi','pooka','simon']
# shelffile['cats']=cat
# print type(shelffile)
# print shelffile['cats']
# shelffile.close()
# for foldername,subfolders,filenames in os.walk('.'):
#     print('the current folder is '+foldername)
#     for subfolder in subfolders:
#         print('subfolder of '+foldername+': '+subfolders)
#     for filenames in filenames:
#         print('filename inside '+foldername+': '+filenames)
# print('')
#
# for filename in os.listdir('.\\automate'):
#     if filename.endswith('.txt'):
#         os.unlink(filename)
#         # print(filename)
# import logging
# logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('start of program')
# def factorial(n):
#     logging.debug('start of factorial(%s%%) %n')
#     total=1
#     for i in range(1,n+1):
#         total*=i
#         logging.debug('i is %d, total is %d' %(i,total))
#     logging.debug('end of factorial(%s%%)'%n)
#     return total
# logging.disable(logging.debug)
# print(factorial(5))
# logging.debug('end of program')
# from selenium import webdriver
# browser=webdriver.Firefox()
# type(browser)
import openpyxl
wb=openpyxl.load_workbook('123.xlsx')
type(wb)