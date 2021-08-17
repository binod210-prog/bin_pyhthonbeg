import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


#Explore the structure of data

filename = 'all_day.json'
with open(filename,encoding="utf8") as f:
    all_eq_data = json.load(f)


# Making a list of all the earthquakes

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts));

# Extracting magnitude data


mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])    


# Extracting location data

mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = lon = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


#map the Earthquakes

data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    
}]

my_layout = Layout(title='Global Eathquake')  

fig = {'data': data, 'layout' : my_layout}    # dictionary 
offline.plot(fig, filename='global_earthquake.html')    
