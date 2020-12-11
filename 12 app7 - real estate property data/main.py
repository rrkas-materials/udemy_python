from bs4 import BeautifulSoup
import pandas, requests

link = 'http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s='
base_link = 'http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r = requests.get(base_link, headers=headers)
c = r.content
bs = BeautifulSoup(c, 'html.parser')
page_nr = int(bs.find_all('a', {'class': 'Page'})[-1].text)
l = []
for i in range(0, page_nr * 10, 10):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    r = requests.get(link + str(i) + '.html', headers=headers)
    c = r.content
    bs = BeautifulSoup(c, 'html.parser')
    for row in bs.find_all('div', {'class': 'propertyRow'}):
        d = {}
        address_locality = row.find_all('span', {'class': 'propAddressCollapse'})
        d['Address'] = address_locality[0].text
        d['Price'] = row.find('h4', {'class': 'propPrice'}).text.strip()
        try:
            area = row.find('span', {'class': 'infoSqFt'}).find('b').text
        except AttributeError:
            area = None
        d['Area'] = area
        try:
            beds = row.find('span', {'class': 'infoBed'}).find('b').text
        except AttributeError:
            beds = None
        d['Beds'] = beds
        try:
            full_baths = row.find('span', {'class': 'infoValueFullBath'}).find('b').text
        except AttributeError:
            full_baths = None
        d['Full Baths'] = full_baths
        try:
            half_baths = row.find('span', {'class': 'infoValueHalfBath'}).find('b').text
        except AttributeError:
            half_baths = None
        d['Half Baths'] = half_baths
        try:
            d['Locality'] = address_locality[1].text
        except AttributeError:
            d['Locality'] = None
        for cg in row.find_all('div', {'class': 'columnGroup'}):
            for fg, fn in zip(cg.find_all('span', {'class': 'featureGroup'}), cg.find_all('span', {'class': 'featureName'})):
                if 'Lot Size' in fg.text:
                    d['Lot Size'] = fn.text.strip()
        l.append(d)
df = pandas.DataFrame(l)
df.to_csv('output.csv')
