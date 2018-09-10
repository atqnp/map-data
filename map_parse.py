from bs4 import BeautifulSoup as Soup
from bs4 import Tag

file = "tokyo.kml"

with open(file,'r',encoding='UTF-8') as f:
    soup = Soup(f, 'lxml-xml')

datalist = []
coorlist = []
dataplace = soup.find_all("ExtendedData")

coor_tag = soup.find_all("coordinates")
no_tag = soup.find_all("LinearRing")

for tag in coor_tag:
    tag.unwrap()
for tag in no_tag:
    tag.unwrap()
    
for place in dataplace:
    subplace = place.text
    final = subplace.split("\n")
    datalist.append(final)
    
for place in dataplace:
    next_sib = place.next_sibling
    while(not isinstance(next_sib, Tag)):
        next_sib = next_sib.next_sibling
    fin_coor = str(next_sib)
    test = fin_coor.replace('<MultiGeometry>','(').replace('</MultiGeometry>',')').replace('<outerBoundaryIs>','(').replace('</outerBoundaryIs>',')').replace('<innerBoundaryIs>','(').replace('</innerBoundaryIs>',')').replace('<Polygon>','(').replace('</Polygon>',')')
    coorlist.append(test)


#Pandas
import pandas as pd
df1 = pd.DataFrame(datalist)
df2 = pd.DataFrame(coorlist)

findata = pd.concat([df1,df2], axis = 1)
findata
