#!/usr/bin/env python
# coding=utf-8
"""

The picture shows some cookies and a picture from challenge 4. I went to challenge 4
page and inspected the cookies, it told me to follow busynothing instead of nothing.

So, I performed the same linked list search as in challenge 4, but using the param busynothing.
Since the hint showed cookies, I was not too surprised to find that at each url there was a cookie.
I collected the cookies and concatenated them to produce:

BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90

I googled bzh91ay and discovered this is a common encoding for bz2 encoding in python
"""
__author__ = 'julenka'

import bz2
import cookielib
import urllib
import urllib2
import re

def get_cookie_at_url(url, cookie_name):
    """ Return cookie of given name from url

    :param url:
    :param cookie_name:
    :return: The cookie with given name, as a string. If name not present, return None
    """
    cookies = cookielib.CookieJar()
    handlers = [urllib2.HTTPCookieProcessor(cookies)]
    opener = urllib2.build_opener(*handlers)
    req = urllib2.Request(url)
    opener.open(req)
    for cookie in cookies:
        if cookie.name == cookie_name:
            return cookie.value
    return None

def perform_hunt():
    """ Get cookie string by following trail of breadcrumbs

    :return:
    """
    cookie_message = ""
    pfx = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    # first val is 12345
    vals=["12345"]
    strs = [""]
    for i in range(400):
        next_url = pfx+vals[-1]
        url_data = urllib2.urlopen(next_url)
        next_str = url_data.read()
        print i,":",next_str
        strs.append(next_str)

        new_cookie = get_cookie_at_url(next_url, "info")
        if new_cookie:
            cookie_message += new_cookie

        m = re.search('and the next busynothing is (\d+)', next_str)
        if not m:
            print "Error: string didn't match:", next_str
            break
        vals.append(m.group(1))
    return cookie_message

if __name__ == '__main__':
    # cookie message, with characters encoded as ascii
    cookie_message = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM" \
                     "%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60" \
                     "%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%" \
                     "AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%" \
                     "AE%24%90"

    if not cookie_message:
        perform_hunt()

    cookie_message = urllib.unquote_plus(cookie_message)

    print bz2.decompress(cookie_message)
    # message says "is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand."
    # I took a hint to see that I had to use problem 13, phonebook
    import p13_disproportional
    print p13_disproportional.phone("Leopold")
    # returns 555-violin, go to violin.php, then stick "the flowers are on their way" into the cookie. *sigh*




