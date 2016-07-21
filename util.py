# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:13:55 2016

@author: Bluefish_
"""

class triangle:
    """ A class that stores a key-value pair as a whole object. """

    __slots = '_id', '_area', '_coordinate', '_prev', '_next' # streamline memory usage    
    
    def __init__(self, key, coor, data):
        ''' Initialize the triangle with the parameters. '''
        self._id = key # current vertex index
        self._coordinate = coor[0:2] # triangle vertex coordinate
        self._area = coor[2] # triangle area
        self._data = data 
        #self._prev = None
        #self._next = None
        
    def setPrev(self, newPrev):
        self._prev = newPrev
        
    def setNext(self, newNext):
        self._next = newNext

    def __gt__(self, i): # >
        return self._area > i._area
    
    def __lt__(self, i): # <
        return self._area < i._area
        
    def __str__(self):
        s = "("+str(self._coordinate[0])+","+str(self._coordinate[1])+")"
        return s+" "+str(self._area)+"\n"