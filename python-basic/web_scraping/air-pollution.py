import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/6410000/GOA/GOA001'
key = 'sx50AIPlpEpq6NbPlgby9QC4MbtIfDTeo1yOoO3RVLHN%2F2bIR7HdifocqieTgUP6Ykv2dKZnoby%2FYUoJiEK9oQ%3D%3D'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : key, urllib.parse.quote_plus('type') : 'json', urllib.parse.quote_plus('numOfRows') : '10', urllib.parse.quote_plus('pageNo') : '1' })

response = urllib.request.urlopen(url + queryParams)
print(response.read().decode())
