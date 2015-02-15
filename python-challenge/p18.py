__author__ = 'julenka'

import urllib, urllib2, cookielib

username = 'huge'
password = 'file'
url = "http://www.pythonchallenge.com/pc/return/romance.html"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'password' : password})
resp = opener.open(url, login_data)

