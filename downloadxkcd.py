#!python
#downloadxkcd.py - downloads every single xkcd comic.
import requests,os,bs4
url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    #TODO: download the page.
    print('downloading page %s...'%url)
    res=requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('there was a problem:%s' %(exc))
    soup=bs4.BeautifulSoup(res.text)
    #TODO: find the url of the comic image.
    comicelem=soup.select('#comic img')
    if comicelem==[]:
        print('could not find comic image.')
    else:
        comicurl='http:'+comicelem[0].get('src')

    #TODO: download the images.
    print('downloading image %s...'%(comicurl))
    res=requests.get(comicurl)
    res.raise_for_status()
    #TODO: save the image to ./xkcd.
    imagefile=open(os.path.join('xkcd',os.path.basename(comicurl)),'wb')
    for chunk in res.iter_content(100000):
        imagefile.write(chunk)
    imagefile.close()
    #TODO: get the prev button's url.
    prevlink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevlink.get('href')
print('Done.')