from bs4 import BeautifulSoup
import urllib2

from css import CSS, parse

def get_css_urls(url):

    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)

    links=soup.findAll('link', href=True)

    urls = []
    for link in links:
        if link.get('type')=='text/css':
            fullurl = "{0}/{1}".format(url,link.get('href'))
            urls.append(fullurl)
            print "added {0} to list.".format(fullurl)

    return urls

def analyse_url(url):

    cssurls = get_css_urls(url)

    csstext = ""
    for cssurl in cssurls:
        csstext += urllib2.urlopen(cssurl).read()

    css = CSS(parse(csstext))
    css.quiet = True

    res = css.compress()

    return res

if __name__ == '__main__':

    res = analyse_url("http://mcsafetyfeed.org/")

    print res
