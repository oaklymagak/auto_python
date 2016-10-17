#!python3
#autoLoginPt.py - auto login in pt web
import requests,bs4,time,sys
from selenium import webdriver
#test wheter the url is correct or not
def test_web_status(url):
    while True:
        try:
            pt_content = requests.get(url)
            pt_content.raise_for_status()
            return pt_content
            break
        except:
            url=input('there exit an 404 error,please enter the website again: ')
            pt_content = requests.get(url)
def autologin():
    url='https://pt.vm.fudan.edu.cn/'
    pt=webdriver.Firefox()
    pt.get(url)
    try:
        usrElem=pt.find_element_by_name('user')
        usrElem.send_keys('qingqiu')
        passwrdElem=pt.find_element_by_name('passwrd')
        passwrdElem.send_keys('13985394459')
        passwrdElem.submit()
    except:
        print('Can not find the inputbox of username and password')
    return pt
def search(keyword):
    pt=autologin()
   # target_content=pt.page_source #获取当前页面Html信息
    time.sleep(5)
    search_page=pt.find_element_by_name('submit')
    search_page.click()
    time.sleep(10)
    search_text=pt.find_element_by_name('search')
    search_text.send_keys(keyword)
    search_text.submit()
    return pt

while True:
    flag=input('you want? 1:login   2:search')
    if flag=='1' or not flag.isalnum:
        pt=autologin()
    elif flag=='2':
        keyword=input('please enter the keyword you want to search.')
        if not keyword.isalnum():
            keyword='生活大爆炸'
        try:
            pt=search(keyword)
        except:
            print('there may be exist an error!!')
    else:
        sys.exit()



