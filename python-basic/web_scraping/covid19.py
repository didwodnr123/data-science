import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
key = 'OxcQOljEruD%2B5ytkRbJHdkIzgR8D7%2FTuF5HAu2ulicBKtYI2cGZlSjqoqWJqiI8oM%2Bm2QUcbzQsk99PdsfiiIw%3D%3D'
key = urllib.parse.unquote(key)
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : key, urllib.parse.quote_plus('pageNo') : '1', urllib.parse.quote_plus('numOfRows') : '10', urllib.parse.quote_plus('startCreateDt') : '20200310', urllib.parse.quote_plus('endCreateDt') : '20200315' })

response = urllib.request.urlopen(url + queryParams)
data = response.read().decode()

print(data)
