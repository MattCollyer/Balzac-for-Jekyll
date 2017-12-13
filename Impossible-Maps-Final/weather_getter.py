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
    api_counter=0
    blanky=[]
    stuff=data['features']
    for things in stuff:
        if 'latty' in things['properties']:
            latty=str(things['properties']['latty'])
            longy=str(things['properties']['longy'])
            percent_dont_believe_happening=100- things['properties']['happening']
            percent_dont_believe_human=100-things['properties']['human']
            temp=get_weather(latty,longy)
            human_temp_adjust=temp*(1-(percent_dont_believe_human/100))
            happening_temp_adjust=temp*(1-(percent_dont_believe_happening/100))
            things['properties']['temperature']= temp
            things['properties']['temp_human_adjust']=human_temp_adjust
            things['properties']['temp_happening_adjust']=happening_temp_adjust
            api_counter+=1
            if(api_counter%500==0):
                print(api_counter)
    data['features']=stuff
    return data
if __name__ == "__main__":
    data = js_r('combined_json1.geojson')
    with open('county_with_weather.geojson', 'w') as file:
        file.write(json.dumps(add_weather(data)))
    file.close()
