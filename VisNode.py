# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 17:00:52 2016

@author: Bluefish_
Class name: VisNode

"""

from TwoDimVector import TwoDimVector as vector

class VisNode:
    ''' 
    A self-defined data structure to assist the Visvalingam algorithm. 
    '''
    
    def __init__(self, index, lvector, rvector, curr):
        ''' 
        Initialize a Visvalingam node. 
        '''
        self.id = index
        self.left = lvector
        self.right = rvector
        self.curr = curr
        self.area = self.left.area(self.right)
        # todo: need to add prev and post nodes.
    
    def updateR(self, post):
        ''' 
        Change the next node of the current node. 
        '''
        self.right = vector(post, self.curr)
        self.area = self.left.area(self.right)
    
    def updateL(self, prev):
        ''' 
        Change the previous node of the current node. 
        '''
        self.left = vector(self.curr, prev)
        self.area = self.right.area(self.left)
    
    def delete(self):
        ''' 
        Set all fields of the current node to None to delete it. 
        '''
        self.id = None
        self.left = None
        self.right = None
        self.area = None
    