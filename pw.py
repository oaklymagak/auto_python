#!python3
#coding:utf-8
#usage: pw.py - ('163'|'save') return account and password | save account and password
import sys,openpyxl,pyperclip,webbrowser
#TODO:set global variable
wb=openpyxl.load_workbook('mypassword.xlsx')
sheet=wb.get_active_sheet()
#TODO: estimate whether want to get or save
def enterInformation():
    print('please enter the abbreviation of the web you want to save')
    abbre = input('enter the abbreviation for index: ')
    print('please enter the website of the web you want to save')
    website = input('enter the website for index: ')
    print('please enter the account of the web you want to save')
    account = input('enter the account for index: ')
    print('please enter the password of the web you want to save')
    password = input('enter the password for index: ')
    return abbre,website,account,password

def max_row(wb_sheet=sheet,row=100):
    for i in range(1,row):
        temp=sheet.cell(row=i,column=1)
        if temp.value is None:
            return i
            break
    return row

while True:
    answer=input('what do you want to do? 1:save 2:copy:')
    if answer=='1':
        wb = openpyxl.load_workbook('mypassword.xlsx')
        sheet = wb.get_active_sheet()
        sheet_row=max_row()
        sheet_column=sheet.max_column
        #TODO:save the follow data into password.xlsx
        result=enterInformation()
        for index in range(1,len(result)+1):
            print('writing %s into password.xlsx.'%result[index-1])
            sheet.cell(row=sheet_row,column=index).value=result[index-1]
            wb.save('mypassword.xlsx')

    #TODO:get the account and password information
    elif answer=='2':
        wb = openpyxl.load_workbook('mypassword.xlsx')
        sheet = wb.get_sheet_by_name('Sheet1')
        abbre=input("which web's account and password information do you want to copy? ")
        sheet_row = max_row()
        for value in range(2,sheet_row):
            if sheet.cell(row=value,column=1).value==abbre:
                print('find and handling,please wait...'.rjust(35,'.'))
                webbrowser.open(sheet.cell(row=value,column=2).value)
                print('opening the web %s'.center(35,'*')%sheet.cell(row=value,column=2).value)
                pyperclip.copy(sheet.cell(row=value,column=3).value)
                while True:
                    temp=input('have you finished the account pasting? Y/N')
                    if temp.lower()=='y' or not temp.isalnum():
                        break
                pyperclip.copy(sheet.cell(row=value,column=4).value)
                while True:
                    temp = input('have you finished the password pasting? Y/N')
                    if temp.lower() == 'y' or not temp.isalnum():
                        break

    #TODO:exit the loop
    else:
        sys.exit()
