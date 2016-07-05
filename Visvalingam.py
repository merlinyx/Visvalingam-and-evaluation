# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 14:03:28 2016

@author: Bluefish_
Class name: Visvalingam

"""

from TwoDimVector import TwoDimVector as v
from VisNode import VisNode as node

class Visvalingam:
    ''' 
    A class specifically for line simplification in maps using the
    Visvalingam algorithm. 
    '''
    
    def __init__(self, pts):
        ''' 
        Store the points and initialize the two lists. 
        '''
        nodes = []
        nodes.append(node(0, v(0,0), v(pts[1,0],pts[1,1]), pts[0]))
        s = len(pts) - 1
        for i in range(1, s):
            nodes.append(node(i, v(pts[i-1],pts[i]), v(pts[i+1],pts[i]), pts[i]))
        nodes.append(node(s, v(pts[s,0],pts[s,1]), v(0,0), pts[s]))
        self.original = nodes
        self.newdict = {}
        self.newlist = []
    
    def findMinAreaNode(self):
        ''' 
        Find the smallest area and return the corresponding point. 
        '''
        minArea = float("infinity")
        minNode = None
        for item in self.original:
            if minArea > item.area:
                minArea = item.area
                minNode = item
        return minNode
    
    def cleanup(self):
        '''
        Deletes all nodes with area 0 and store them in a list 
        with their areas. This prepares for the while loop.
        '''
        for item in self.original:
            if item.area == 0:
                self.newdict[item.id] = item.area
                self.newlist.append(item.area)
                item.delete() # todo: need to consider end nodes
    
    def main(self):
        '''
        Execute the simplification process.        
        '''
        
        self.cleanup()
        while len(self.original) > 0:
            curr = self.findMinAreaNode()
            last_area = self.newlist[len(self.newlist)-1]
            if curr.area < last_area:
                curr.area = last_area
            self.newdict[curr.id] = curr.area
            self.newlist.append(curr.area)
            self.original.remove(curr.area)
            curr.delete()
            
            