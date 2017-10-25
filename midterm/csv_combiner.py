#!/usr/bin/env python3
"""

    csv_combiner.py - combining two csv files into one based on a key
    Author: <Matthew Collyer> (<matthewcollyer@bennington.edu>)
    Created: 10/12/2017

"""


import csv

savefile=open('counties2.csv', 'w')
csvfile=open('opini.csv',encoding='utf-8')
csvfyle=open('counties.csv',encoding='utf-8')
reader = csv.reader(csvfile, delimiter=',', quotechar='"')
reeder = csv.reader(csvfyle, delimiter=',', quotechar='"')
p=0
g=0
for lyne in reeder:
    g=0
    for line in reader:
        # print(lyne[1]+" "+line[0])
        if g==0 and p==0:
            savefile.write(lyne[0]+','+lyne[1]+','+lyne[2]+','+lyne[3]+','+lyne[4]+','+line[1]+','+line[2])
            savefile.write('\n')
            g=1
            break
        elif g==0:
            g=1
        if (g!=0 and p!=0):
            print(lyne[1]+" "+line[0])
            if (int(lyne[1])==int(line[0])):
                savefile.write(lyne[0]+','+lyne[1]+','+lyne[2]+','+lyne[3]+','+lyne[4]+','+line[1]+','+line[2])
                savefile.write('\n')
                break
    if p==0:
        p=1
csvfile.close
csvfyle.close
savefile.close
