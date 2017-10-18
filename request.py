import requests
website = 'http://httpbin.org/headers'
myheaders={'user-agent': 'Iphone X'}
r = requests.get(url=website, headers=myheaders)
print(r.url)
print('Status code:')
print('\t[-]' + str(r.status_code) + '\n')
print('{:*^100}'.format('*'))
print('{: ^30}'.format('Server Header'))
for x in r.headers:
    print('\t' + x +' : ' + r.headers[x])
print('{:*^100}'.format('*'))
print(r.headers['content-type'])
print('Content:\n')
print(r.text)
