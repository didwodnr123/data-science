import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import sqlite3
from config import keys

conn = sqlite3.connect('covid19db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Covid19')

cur.execute('''
    CREATE TABLE Covid19 (
        seq VARCHAR(30) PRIMARY KEY,
        createDt VARCHAR(50),
        decideCnt VARCHAR(50),
        careCnt VARCHAR(50)
    )
''')

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
key = keys.covid19_key
key = urllib.parse.unquote(key)
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') : key, urllib.parse.quote_plus('pageNo') : '1', urllib.parse.quote_plus('numOfRows') : '10', urllib.parse.quote_plus('startCreateDt') : '20201205', urllib.parse.quote_plus('endCreateDt') : '20201212' })

response = urllib.request.urlopen(url + queryParams)
data = response.read().decode()
print('data:', data)
body = ET.fromstring(data)
print('body:', body)

lst = body.findall('body/items/item')
print('Item count:', len(lst))

for item in lst:
    seq = item.find('seq').text
    createDt = item.find('createDt').text
    decideCnt = item.find('decideCnt').text
    careCnt = item.find('careCnt').text
    cur.execute('''INSERT INTO Covid19 (seq, createDt, decideCnt, careCnt)
                VALUES (?, ?, ?, ?)''', (seq, createDt, decideCnt, careCnt))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT * FROM Covid19'

for row in cur.execute(sqlstr):
    print(row[0], row[1], row[2], row[3])

cur.close()
