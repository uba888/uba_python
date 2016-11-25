# -*- coding: utf-8 -*-
import re
import urllib.request
import os

i = 1

def findHtml(url):
    base = os.path.dirname(__file__)
    print('文件所在目录为：'+base)
    if not os.path.exists(base+'files'):
        os.mkdir(base+'files')
    html = getHtml(url)
    hreflist = getHref(r'href=\'([^<>]*\.html)\'',html)
    if  hreflist != 0:
        print('共匹配了%d个链接可供下载!!' % len(hreflist))
        for href in hreflist:
            try:
                print('http://www.ygdy8.net'+href)
                code = getHtml('http://www.ygdy8.net'+href)
                downHref(code)
            except Exception:
                pass


#读取网页源码
def getHtml(url):
    print('正在读取网页源码！')
    html = urllib.request.urlopen(url,timeout=20).read()
    try:
        html = html.decode('gbk')
    except UnicodeDecodeError:
        html = html.decode('utf-8')
    return html

    
#获取网页中指定的超链接
def getHref(reg,html):
    print('正在匹配链接！！')
    hreflist = re.findall(reg, html)
    if len(hreflist) == 0:
        print('没有可供采集的链接了！T_T')
        return 0
    else:
        return hreflist


#生成文件，写入下载的链接，文件名为网页Title
def downHref(html):
    global i
    reg = r'href="([^<>]*\.[mkvrb]*)"'
    title = re.findall(r"<title>(.*)</title>", html)
    title = "("+str(i)+")"+title[0]
    hreflist = getHref(reg,html)
    if hreflist != 0:
        hreff = "\n".join(hreflist)
        open('files/'+title+'.txt','w').write(hreff)
        print('正在生成第%d个文本！'%(i))
        i+=1

address = 'http://www.ygdy8.net'
html = findHtml(address)
print('总共生成了%d个文件！'%i)
input('press any key to exit!')

