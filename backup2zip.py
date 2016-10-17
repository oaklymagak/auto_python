#python
#coding=utf-8
#backup2zip.py - copies an entire contents of "folder" into a zip file.

import zipfile,os
def backuptozip(folder):
    #backup the entire contents of "folder" into a zip files.
    folder=os.path.abspath(folder)
    #figure out the filename this code should use based on what files already exist.
    number=1
    while True:
        zipfilename=os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipfilename):
            break
        number=number+1
    #TODO: create the zip file.
    print('creating %s...'%zipfilename)
    backupzip=zipfile.ZipFile(zipfilename,'w')
    #TODO: walk the entire folder tree and compress the files in each folder.
    for foldername,subfoldername,filenames in os.walk(folder):
        print('adding files in %s...'%foldername)
        backupzip.write(foldername)
    for filename in filenames:
        newBase = os.path.basename(folder)+'_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue
        backupzip.write(os.path.join(foldername,filename))
    backupzip.close()
    print('Done.')

backuptozip('.')