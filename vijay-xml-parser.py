import xml.etree.ElementTree as ET
#tree = ET.parse('country_data.xml')
tree = ET.parse('arf.xml')
root = tree.getroot()
#root = ET.fromstring(country_data_as_string)

print(root.attrib)

for child in root:
 print(child.tag, child.attrib)

# get the resutls node from the xml
testResult = root.find(".//{http://checklists.nist.gov/xccdf/1.2}TestResult")
testVersion = testResult.attrib.get("version") 

for item in testResult: 
    print(item.attrib)