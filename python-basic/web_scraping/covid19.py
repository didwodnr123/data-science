import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
key = 'sx50AIPlpEpq6NbPlgby9QC4MbtIfDTeo1yOoO3RVLHN%2F2bIR7HdifocqieTgUP6Ykv2dKZnoby%2FYUoJiEK9oQ%3D%3D'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : key, urllib.parse.quote_plus('type') : 'json', urllib.parse.quote_plus('numOfRows') : '10', urllib.parse.quote_plus('pageNo') : '1' })

response = urllib.request.urlopen(url + queryParams)
print(response.read().decode())
