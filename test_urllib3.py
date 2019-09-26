import urllib3
url = 'www.baidu.com'


print('第一种方法')
conn1 = urllib3.connection_from_url(url)
r = conn1.request('GET','/')
return_code1 = r.status
response1 = r.data.decode('utf-8')
print(return_code1)
#print(response1)


request = urllib3.connection.