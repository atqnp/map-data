import xml.etree.ElementTree as ET
tree = ET.parse("results.kml")
root = tree.getroot()
nmsp = "{http://www.opengis.net/kml/2.2}"
data = root.find("{}Document".format(nmsp)).find("{}Folder".format(nmsp))
plcms = data.findall("{}Placemark".format(nmsp))

for placemark in plcms:
    for item in placemark.iter("{}ExtendedData".format(nmsp)):
        for i in item:
            for n in i:
                print(n.attrib['name'], n.text)
                

for placemark in plcms:
    for item in placemark.iter("{}Polygon".format(nmsp)):
        for i in item:
            for n in i:
                for x in n:
                    print(x.text)
