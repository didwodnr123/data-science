import urllib.request, urllib.parse, urllib.error
import json

url = 'http://apis.data.go.kr/6410000/GOA/GOA001'
key = '%2BvoFlW8qaQb%2F%2BsFq82OIdJK7tQL9NsF7Vr%2FGK37%2BD0DTEkspRGRNX4arDqFDOOohXQXRGnCwKtJfIL7hJqU6nw%3D%3D'
key = urllib.parse.unquote(key)
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : key, urllib.parse.quote_plus('type') : 'json', urllib.parse.quote_plus('numOfRows') : '10', urllib.parse.quote_plus('pageNo') : '1' })

response = urllib.request.urlopen(url + queryParams)
data = response.read().decode()

try:
    js = json.loads(data)
except:
    print('urlopen error')

for item in js['items']:
    if item == { }:
        print('None')
        continue
    if item['area'] == '성남시':
        print(item)

print('item counts:', len(js['items']))
