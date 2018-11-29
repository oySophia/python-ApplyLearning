#coding = utf-8
#!/usr/bin/python

import urllib2
import sys
import string
from re import sub

#s_url =

def analysisPage(html, txtfile):
    html = sub(r'[\s]+', '', html)
    news_html = sub(r'^.*pc_temp_songlist">', '', html)
    print news_html
    while news_html.find('pc_temp_songname"title="') != -1:
        end = news_html.find("</li>")
	#print end
        news = news_html[:end]
	#print news
        news_html = news_html[end + 5:]
    	info = sub(r'[\s]+', ',', sub(r'<[^<>]*>', ' ', news))
        #print info
        songname = info.split(',')[2] + '\n'
        print songname
        txtfile.write(songname)
	#txtfile.write("\n\n")
    #print info

def getResult(url):
    txtfile = open("cnbeta.txt", "w")
    html = urllib2.urlopen(url).read()
    print html
    #html = html.decode('gbk', 'ignore').encode('utf-8')
    #print html
    analysisPage(html, txtfile)
    txtfile.close()

if __name__ == '__main__':
    #if len(sys.argv) != 2:
     #   print "Usage: g_cnbate.py the url you want to grab"
     #   exit(1)
    getResult("http://www.kugou.com/yy/rank/home/1-8888.html")
