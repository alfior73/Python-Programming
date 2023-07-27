import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Alfio</name>
    <phone type="intl">
        +1 978 258 7775
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find('name').text)
print("Attr:", tree.find('email').get('hide'))
