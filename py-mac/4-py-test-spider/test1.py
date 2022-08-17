# -*- coding: UTF-8 -*-

# import urllib3
#
# # import urllib
# values = {}
# values['username'] = 'sida'
# values['password'] = "sida123"
# data = urllib3.encode_multipart_formdata(values)
# userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': userAgent}
# request = urllib3._request("http://www.baidu.com");
# response = urllib2.urlopen(request, data)
# print
# response.read()


import urllib.request

# https://docs.python.org/3.8/library/urllib.request.html#module-urllib.request

with urllib.request.urlopen("http://www.baidu.com") as f:
    print(f.read(300))


