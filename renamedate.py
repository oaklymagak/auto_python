#!python3
#coding=utf-8
#renamedate.py - renames filenames with american MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil,os,re
# create a regex that matches files with the anmerican date format.
dateformat=re.compile(r'''^(.*?) #all text before the date
    ((0|1)?\d)-  #one or two digits for the month
    ((0|1|2|3)?\d)-  #one or two digits for the day
    ((19|20)\d{2})   #four digits for the year
    (.*?)$        #all text after the date
    ''',re.VERBOSE)
#TODO: LOOP the files in the working directory.
for filename in os.listdir('.'):
    mo=dateformat.search(filename)
#TODO: skip files without a date.
    if mo==None:
        continue
#TODO: get the different parts of the filename.
    beforepart=mo.group(1)
    monthpart=mo.group(2)
    daypart=mo.group(4)
    yearpart=mo.group(6)
    afterpart=mo.group(8)

#TODO: FORM the European-style filename.
    eurofilename=beforepart+daypart+'-'+monthpart+'-'+yearpart+afterpart
#TODO: GET the full,absolute file paths.
    absworkingdir=os.path.abspath('.')
    amerfilename=os.path.join(absworkingdir,filename)
    eurofilename=os.path.join(absworkingdir,eurofilename)
#TODO: rename the files.
    print('renaming %s to %s...'%(amerfilename,eurofilename))
    shutil.move(amerfilename,eurofilename)