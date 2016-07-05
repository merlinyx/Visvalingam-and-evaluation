# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 17:00:52 2016

@author: Bluefish_
Class Name: VisNode

"""

from TwoDimVector import TwoDimVector as vector

class VisNode:
    ''' 
    A self-defined data structure to assist the Visvalingam algorithm. 
    '''
    
    def __init__(self, index, prev, curr, post):
        ''' 
        Initialize a Visvalingam node. 
        '''
        self.id = index
        self.left = prev
        self.curr = curr        
        self.right = post
        self.area = self.updateArea()
    
    def updateArea(self):
        '''
        Update the area associated with this node.         
        '''
        vLeft = vector(self.prev, self.curr)
        vRight = vector(self.post, self.curr)
        return vLeft.area(vRight)
    
    def updateR(self, post):
        ''' 
        Change the next node of the current node. 
        '''
        self.right = post
        self.area = self.updateArea()
    
    def updateL(self, prev):
        ''' 
        Change the previous node of the current node. 
        '''
        self.left = prev
        self.area = self.updateArea()
    
    def delete(self):
        ''' 
        Set itself to an ineffective node, and connect its prev and post nodes.
        '''
        # self.id = None
        self.left = [0,0]
        self.right = [0,0]
        self.area = 0
        prev_ = self.left
        post_ = self.right
        prev_.updateR(post_)
        post_.updateL(prev_)