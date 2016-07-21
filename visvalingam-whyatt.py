# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:21:43 2016

@author: Bluefish_
Visvalingam Algorithm implemented with minimum heap. 
What we get is a filter-like list. 

"""

import csv
import math
from VisMinHeap import min_heap
from util import triangle

projectionSize = 6378137
cc = math.pi/180

def lon2x(lon):
    r = projectionSize / (2 * math.pi);
    falseEasting = -1.0 * projectionSize / 2.0;
    return (r * lon * cc) - falseEasting;

def lat2y(lat):
    r = projectionSize / (2 * math.pi);
    falseNorthing = projectionSize / 2;
    return ((r / 2 * math.log((1 + math.sin(lat * cc)) / 
                              (1 - math.sin(lat * cc)))) - falseNorthing) * (-1);

def csv2xy(inFilename):
    points = []
    with open(inFilename, "r") as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            if row[0]=='id':
                continue
            xx = lon2x(float(row[2]))
            yy = lat2y(float(row[1]))
            points.append([xx,yy,0])
    return points

def area(t):
    ''' formula: s = (1/2) (x1(y2-y3) + x2(y3-y1) + x3(y1-y2)) '''
    a = (t[0][0]*(t[1][1]-t[2][1]) + t[1][0]*(t[2][1]-t[0][1]) 
                                      + t[2][0]*(t[0][1]-t[1][1]))/2
    if a < 0:
        return -a
    return a
    
def update(t, heap):
    heap.remove(t)
    t._data[1][2] = area(t._data)
    t._area = t._data[1][2]
    heap.push(t)

feature = "playas"
fname = "data_"+feature+".csv"
data = csv2xy(fname)

heap = min_heap()
triangles = [];
n = len(data)
dataleft = [data[0],data[0],data[1]]
triangles.append(triangle(0, data[0], dataleft)) # the leftmost node
for i in range(1, n - 1):
    t = data[i-1:i+2] # slice the three vertices of a triangle
    t[1][2] = area(t)
    tri = triangle(i, t[1], t) # add index and the coordinate
    triangles.append(tri)
dataright = [data[n-2],data[n-1],data[n-1]]
triangles.append(triangle(n-1,data[n-1], dataright)) # the rightmost node
    
original = open("original_vis.txt","w")
for t in triangles:
    original.write(t.__str__())
original.close()

for i in range(1, len(data) - 1):
    tri = triangles[i] # this is a triangle object
    tri.setPrev(triangles[i-1])
    tri.setNext(triangles[i+1])
    heap.push(tri)

max_area = 0
while (not heap.is_empty()):
    item = heap.remove_min_area() # min triangle data returned    
    # the if is here due to the paper by Visvalingam and Whyatt    
    if (item._area < max_area):
        item._area = max_area
    else:
        max_area = item._area 
    
    # connect its prev and next
    if item._prev._area != 0: # not leftmost
        item._prev._next = item._next
        item._prev._data[2] = item._data[2]
        update(item._prev, heap)
    else:
        item._data[0][2] = item._data[1][2]
    if item._next._area != 0: # not rightmost
        item._next._prev = item._prev
        item._next._data[0] = item._data[0]
        update(item._next, heap)
    else:
        item._data[2][2] = item._data[1][2]

outputfile = open("output_vis.txt","w")
for t in triangles:
    outputfile.write(t.__str__())
outputfile.close()