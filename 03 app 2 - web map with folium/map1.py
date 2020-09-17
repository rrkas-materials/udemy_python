#pip3 install folium
##pip3 install jinja2
import folium
import pandas


data = pandas.read_csv('volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
names = list(data["NAME"])

popupFormat = '''<h4>Volcano Information:</h4>
Height: %s m\n
<br>
Name: %s
'''

map = folium.Map(
    location = [38.58, -99.09],
    zoom_start = 5,
    tiles = 'OpenStreetMap'
)

fgv = folium.FeatureGroup(name = "Volcanoes")

def get_color(el):
    if el < 1500:
        return 'green'
    elif 1500 <= el <= 2500:
        return 'orange'
    else:
        return 'red'

for lt, ln, name, el in zip(lat, lon, names, elev):
    iframe = folium.IFrame(html = popupFormat % (el,name), width=200, height=100)
    fgv.add_child(
        folium.CircleMarker(
            location = [lt, ln],
            popup = folium.Popup(iframe),
            fill_color = get_color(el),
            color = 'grey',
            fill_opacity = 0.7,
            radius = 6,
        ),
    )




fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(
    folium.GeoJson( 
        data = (open('world.json', 'r', encoding='utf-8-sig')).read(),
        style_function = lambda x : {
            'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 
            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
            else 'red',
        },
    ),
)




map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")