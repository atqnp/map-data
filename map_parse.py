import xml.etree.ElementTree as ET
import pandas as pd
from bs4 import BeautifulSoup as Soup
from bs4 import Tag
maketrans = str.maketrans

file = "tokyo.kml"

with open(file,'r',encoding='UTF-8') as f:
    soup = Soup(f, 'lxml-xml')

datalist = []
coorlist = []
dataplace = soup.find_all("ExtendedData")

coor_tag = soup.find_all("coordinates")
no_tag = soup.find_all("LinearRing")
schema_tag = soup.find_all("SchemaData")

for tag in coor_tag:
    tag.unwrap()
for tag in no_tag:
    tag.unwrap()
for tag in schema_tag:
    tag.unwrap()
                
for place in dataplace:
    data1 = []
    data2 = []
    for sub in place.find_all("SimpleData"):
        subname = sub['name']
        subplace = sub.text
        data1.append(subname)
        data2.append(subplace)
    datadict = dict(zip(data1,data2))
    datalist.append(datadict)
    
for place in dataplace:
    next_sib = place.next_sibling
    while(not isinstance(next_sib, Tag)):
        next_sib = next_sib.next_sibling
    fin_coor = str(next_sib)
    fin_coor = fin_coor.translate(maketrans(', ',' ,'))
    test = fin_coor.replace('<MultiGeometry><Polygon>','MULTIPOLYGON ((').replace('</MultiGeometry>',')').replace('<outerBoundaryIs>','(').replace('</outerBoundaryIs>',')').replace('<innerBoundaryIs>',',(').replace('</Polygon><Polygon>','),(').replace('</innerBoundaryIs>',')').replace('<Polygon>','POLYGON (').replace('</Polygon>',')')
    coorlist.append(test)

#Pandas
df1 = pd.DataFrame(datalist)
df2 = pd.DataFrame(coorlist)
df2.columns = ["GEOMETRY"]
findata = pd.concat([df1,df2], axis = 1)
findata = findata[['KEN','GUN','SIKUCHOSON','JCODE','P_NUM','H_NUM','GEOMETRY']]
findata.to_csv("findata.csv")
