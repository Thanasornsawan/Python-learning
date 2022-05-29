import requests
from requests.exceptions import HTTPError
x = requests.get('http://httpbin.org/get')
print(x.headers['Server'])

if x.status_code == 200:
    print("Success!")
elif x.status_code == 400:
    print("Not found!")
    
print(x.elapsed)
print(x.cookies)

x = requests.get('http://httpbin.org/get',params={'id':'1'})
print(x.url)
x = requests.get('http://httpbin.org/get?id=2')
print(x.url)
x = requests.get('http://httpbin.org/get',params={'id':3},headers={'Accept':'application/json', 'test_header':'test'})
print(x.text)
x = requests.delete('http://httpbin.org/delete')
print(x.text)
x = requests.post('http://httpbin.org/post', data={'a':'b', 'c':'d'})
print(x.text)

#download
x=requests.get('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
with open('google.png', 'wb') as f:
    f.write(x.content)

#upload
files={'file': open('google.png','rb')}
x=requests.post('http://httpbin.org/post', files=files)
print(x.text)

x=requests.get('http://httpbin.org/get', auth=('username','password'))
print(x.text)

#verify=False is ignore error about ssl expired
x=requests.get('https://expired.badssl.com', verify=False)
print(x.text)

#because it try to redirect to https
x=requests.get('http://github.com',allow_redirects=False)

x=requests.get('http://httpbin.org/cookies', cookies={'a':'b'})
print(x.content)

x=requests.Session()
x.cookies.update({'a':'b'})
print(x.get('http://httpbin.org/cookies').text)