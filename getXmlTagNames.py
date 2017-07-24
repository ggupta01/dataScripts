import xml.etree.ElementTree as ET
import re
#e = ET.parse('test.xml').getroot()

file_name = raw_input("Please enter the file name: ")

def parseXML(parent):
        for child in parent:
                if len(list(child)) > 0:
                        parseXML(child)
                else:
                        if '}' in child.tag:
                                child.tag = child.tag.split('}', 1)[1]
                        print child.tag


with open(file_name,"rb") as f:
        for line in f:
                data = ET.fromstring(line)
                if len(list(data)) > 0:
                        parseXML(data)
                else:
                        print data

