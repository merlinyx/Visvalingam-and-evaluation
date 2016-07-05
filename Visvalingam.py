# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 14:03:28 2016

@author: Bluefish_
Class Name: Visvalingam

"""

from VisNode import VisNode as node

class Visvalingam:
    ''' 
    A class specifically for line simplification in maps using the
    Visvalingam algorithm. 
    '''
    
    def __init__(self, pts):
        ''' 
        Store the points and initialize the two lists . 
        '''
        self.N = len(pts) - 1
        nd = []
        nd.append(node(0, pts[0], pts[0], pts[1]))
        for i in range(1, self.N):
            nd.append(node(i, pts[i-1], pts[i], pts[i+1]))
        nd.append(node(self.N, pts[self.N-1], pts[self.N], pts[self.N]))
        self.original = nd
        self.newdict = {}
        self.last_area = 0
    
    def findMinAreaNode(self):
        ''' 
        Find the smallest area and return the corresponding point. 
        '''
        minArea = float("infinity")
        minNode = None
        for item in self.original[1:-2]:
            if minArea > item.area:
                minArea = item.area
                minNode = item
        return minNode
    
    def cleanup(self):
        '''
        Deletes all nodes with area 0 except for the first and last nodes. 
        Store the id in a dictionary with their areas. 
        Store the areas in a list. This prepares for the while loop.
        '''
        for i in range(1, self.N):
            item = self.original[i]
            if item.area == 0:
                self.newdict[i] = item.area
                item.delete(self.original[i-1], self.original[i+1])
        self.newdict[0] = 0
        self.newdict[self.N] = 0
     
    def main(self):
        '''
        Execute the simplification process.        
        '''
        self.cleanup()
        while len(self.newdict.keys()) < (self.N + 1):
            curr = self.findMinAreaNode()
            i = curr.id
            print(i)
            if curr.area < self.last_area:
                curr.area = self.last_area
            self.newdict[i] = curr.area
            self.last_area = curr.area
            # self.original.pop(curr.id)
            curr.delete(self.original[i-1], self.original[i+1])
    
    def getVisFilter(self):
        '''
        Return the resulted filter in the form of dictionary.         
        '''
        self.main()
        return self.newdict
        
    def getSimplified(self, threshold):
        '''
        Return a list of indices for points that are important according to
        a given threshold for effective areas.
        Also return the simplification rate under this threshold. 
        '''
        indices = [0]
        for index, area in self.newdict.keys(), self.newdict.values():
            if area > threshold:
                indices.append(index)
        indices.append(self.N)
        return indices, len(indices)/self.N