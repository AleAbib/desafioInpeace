import sys
import xml.etree.ElementTree as ET

entry = sys.argv

def ChangeText(entry):
    archive = entry[1]
    tree = ET.parse(archive)
    root = tree.getroot()

    inputtext = entry[3]
    changedtext = entry[4]

    for child in root.iter('*'):
        for attribute in child.attrib:
            if(child.attrib[attribute] == str(inputtext)):
                child.text = "#" +  changedtext

    archiveFinal = entry[2]
    tree.write(archiveFinal)

if (len(entry) >= 5):
    if(entry[1].__contains__('.xml') and entry[2].__contains__('.xml')):
        ChangeText(entry)
    else:
        print('Error: Confirm your entrys')
else:
    print('Error: Confirm your entrys')

