import urllib.request,requests,urllib.parse,re
def listToString(list):
	string=''
	for element in list:string+=element
	return string
PROXY_ADDRESS='192.168.0.101:9097'
url='https://ro.wikipedia.org/wiki/Python'
resp=requests.get(url,proxies={'http':PROXY_ADDRESS})
print('Proxy server returns response headers: %s '%resp.headers)
values=''
data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respData=resp.read()
paragraphs=re.findall('<p>(.*?)</p>',str(respData))
for eachP in paragraphs:print(eachP)
API_ENDPOINT='https://pastebin.com/api/api_post.php'
API_KEY='3EyLsDeerYFf6prdqAzJfcPR2cRREQDN'
source_code='\nprint("Hello, world!")\na = 1\nb = 2\nprint(a + b)\n'
data={'api_dev_key':API_KEY,'api_option':'paste','api_paste_code':source_code,'api_paste_format':'python'}
r=requests.post(url=API_ENDPOINT,data=data)
pastebin_url=r.text
print('The pastebin URL is:%s'%pastebin_url)
r=requests.head('https://httpbin.org/',data={'key':'value'})
print(r)
print(r.headers)
print(r.content)
url='https://requestbin.com/r/enyasw7ymmvf8'
response=requests.options(url)
methods=re.findall("Methods': '.*\\w+',",str(response.headers))
methods=listToString(methods)
print(methods.replace('[','').replace(']','').replace("',",'').replace("'",''))
