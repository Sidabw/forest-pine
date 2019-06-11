# -*- coding: UTF-8 -*-
import urllib2
import urllib

values = {}
values['username'] = 'sida'
values['password'] = "sida123"
data = urllib.urlencode(values)
userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : userAgent}
request = urllib2.Request("http://www.baidu.com");
response = urllib2.urlopen(request, data)
print response.read()