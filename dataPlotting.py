# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:58:02 2016

@author: Bluefish_
Extract data from csv files and do the line simplification.
Plot them.
Thanks to ianisl I get the same conversion with geoplotlib.
lon2x() and lay2y() are copy-pasted from isanisl's `mercator`.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import math

projectionSize = 6378137
cc = math.pi/180

def lon2x(lon):
    r = projectionSize / (2 * math.pi);
    falseEasting = -1.0 * projectionSize / 2.0;
    return (r * lon * cc) - falseEasting;

def lat2y(lat):
    r = projectionSize / (2 * math.pi);
    falseNorthing = projectionSize / 2;
    return ((r / 2 * math.log((1 + math.sin(lat * cc)) / (1 - math.sin(lat * cc)))) - falseNorthing) * (-1);

def csv2xy(inFilename):
    x = []
    y = []
    with open(inFilename, "r") as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            if row[0]=='id':
                continue
            xx = lon2x(float(row[2]))
            yy = lat2y(float(row[1]))
            x.append(xx)
            y.append(yy)
    return np.array(x), np.array(y)

namingStr = "playas"
iFilename = "data_"+namingStr+".csv"
x, y = csv2xy(iFilename)

plt.figure(figsize=(15, 10), facecolor='w', edgecolor='k')
plt.plot(x,y,'.g-')
plt.savefig(namingStr+".jpg")