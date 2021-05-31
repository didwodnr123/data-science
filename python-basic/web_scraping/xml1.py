import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chunk</name>
    <phone type="intl">
        +1 734 393 2039
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
