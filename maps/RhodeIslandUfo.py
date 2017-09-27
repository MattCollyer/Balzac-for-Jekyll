#!/usr/bin/env python3
import csv
"""

    rhodeIslandUfo.py - Python3 Example program.
    Author: <Matthew Collyer> (<matthewcollyer@bennington.edu>)
    Created: 9/26/2017

"""
# I could not figure out how to include an escape character with split, so I used the csv module
savefile=open('rhodeislandufo.csv', 'w')
with open('complete.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    j=0
    for line in reader:
        if j==0:
            p=0
            j=1
            while p<len(line):
                savefile.write(line[p]+',')
                p+=1

        if 'ri' in line[2]:
          savefile.write('\n')
          i=0
          while i<len(line):
            savefile.write(line[i]+',')
            i+=1
savefile.close()
