import xml.etree.ElementTree as ET

data ='''<person>
          <name>Chuck</name>
          <phone type="intl">
            +1 123 456 789
          </phone>
          <email hide="yes"/>
        </person>
'''

tree = ET.fromstring(data)
print('Name:' ,tree.find('name').text)
print('Attr:' ,tree.find('email').get('hide'))


xml_input ='''
<stuff>
    <users>
        <user x="2">
            <id>002</id>
                <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
                <name>Brent</name>
        </user>
    </users>
</stuff>

'''

stuff = ET.fromstring(xml_input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
1
