#!/usr/bin/env python3
"""

    weather_getter.py - gettin dark sky api
    Author: <Matthew Collyer> (<matthewcollyer@bennington.edu>)
    Created: 10/17/2017

"""
import requests
import json
from json_combiner import js_r

def get_weather(latty, longy):
    darksky="https://api.darksky.net/forecast/58fb5fc4abf5d919f26cb526fca733d2/"
    excludes="?exclude=[minutely,hourly,daily,alerts,flags]"
    longy=longy[1:]
    longy='-'+longy
    url=darksky+latty+","+longy+excludes
    stuff=requests.get(url)
    weather=json.loads(stuff.content)
    return weather['currently']['temperature']
def add_weather(data):
    i=0
    for dicts, keys in data.items():
        if i!=0:
            while i<len(keys):
                if 'latty' in keys[i]['properties']:
                    latty=str(keys[i]['properties']['latty'])
                    longy=str(keys[i]['properties']['longy'])
                    keys[i]['properties']['temperature']= get_weather(latty,longy)
            i+=1
        i=1




    return json.dumps(data,ensure_ascii=False)

if __name__ == "__main__":
    data = js_r('combined_json1.geojson')
    add_weather(data)
    savefile=open('county_with_weather.geojson', 'w')
    savefile.write(add_weather(data))
