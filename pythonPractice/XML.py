import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Hong</name>
  <phone type="intl">
    +82 10 6404 6832
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

