# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:56:15 2016

@author: Bluefish_
Visvalingam Test.

"""

import shapefile
from Visvalingam import Visvalingam

# read in data
iFilename = "ne_10m_coastline/ne_10m_coastline" #unknown 537 236
# iFilename = "ne_10m_playas/ne_10m_playas" #Salar de Uyuni 3 277 World's largest salt flat
# iFilename = "ne_10m_rivers_lake_centerlines/ne_10m_rivers_lake_centerlines"
# (636, 340) river centerline Ile almost straight
# (190, 320) river North Saskatchewan good curves
sf = shapefile.Reader(iFilename)
shapes = sf.shapes()
# select the entries we want
data_points = shapes[537].points # a list of (lat,lon)
geoLine = Visvalingam(data_points)
# implifiedPoints, simplifyRate = geoLine.getSimplified(0.0005)
#print(simplifyRate)
dictionary = geoLine.getVisFilter()
print(dictionary)
