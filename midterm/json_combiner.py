#!/usr/bin/env python3
"""

    json_combiner.py - combining two json files into one based on a key
    Author: <Matthew Collyer> (<matthewcollyer@bennington.edu>)
    Created: 10/13/2017

"""
import json

def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))
def js_combine(main_dict, dict2):

    i=0
    for dicts,keys in main_dict.items():
        if i!=0:
            while i<len(keys):
                # Here the geo_id needs to be trimmed
                trim=(keys[i]['properties']['GEO_ID']).split('S')
                keys[i]['properties']['GEO_ID']=trim[1]
                if keys[i]['properties']['GEO_ID'][0]=='0':
                    ayo=keys[i]['properties']['GEO_ID'][1:]
                    keys[i]['properties']['GEO_ID']=ayo
                p=0
                while p<len(dict2) and i<len(keys):
                    if dict2[p]['FIPS']==keys[i]['properties']['GEO_ID']:
                        keys[i]['properties']['latty'] = dict2[p]['Latitude']
                        keys[i]['properties']['longy']=dict2[p]['Longitude']
                        keys[i]['properties']['happening']=round(float(dict2[p]['happening']),3)
                        keys[i]['properties']['human']=round(float(dict2[p]['human']),3)
                    p+=1
                i+=1
        i=1

    return json.dumps(main_dict,ensure_ascii=False)


if __name__ == "__main__":
    county_data = js_r('countiez.json')
    polygon_data= js_r('countyz.geojson')
    savefile=open('combined_json.geojson', 'w')
    savefile.write(js_combine(polygon_data,county_data))
