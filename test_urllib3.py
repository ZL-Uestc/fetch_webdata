import urllib3
url = 'www.baidu.com'


print('第一种方法')
conn1 = urllib3.connection_from_url(url)
r = conn1.request('GET','/')
response1 = r.headers
print(response1)
