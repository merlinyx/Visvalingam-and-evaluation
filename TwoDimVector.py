# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 12:32:32 2016

@author: Bluefish_
Class Name: TwoDimVector

"""

import math

class TwoDimVector:
    ''' A class of 2D vector that assists the Visvalingam algorithm and
        some other measures for evaluating the algorithm. '''
  
    def __init__(self, x_, y_):
        ''' Initialize a 2D vector from its coordinates. '''
        self.x = x_
        self.y = y_
        self.norm = (self.x*self.x + self.y*self.y)**0.5
    
    @classmethod
    def fromTwoPoints(cls, a, b):
        ''' Initialize a 2D vector from the coordinates of two points. '''        
        return cls(a[0]-b[0], a[1]-b[1])
    
    def normProd(self, v):
        ''' A helper calculation of the product of two vectors' norms. '''
        return self.norm * v.norm
    
    def dot(self, v):
        ''' Calculate the dot product value with another vector v. '''
        return self.x * v.x + self.y * v.y
    
    def cosine(self, v):
        ''' Calculate the cosine value of the angle between itself 
            and another vector v. '''
        return self.dot(v) / self.normProd(v)
    
    def ang(self, v):
        ''' Calculate the angle (in radians) between itself and another 
            vector v. The acos() will always give positive values. '''
        return math.acos(self.cosine(v))
    
    def exteriorAng(self, v):
        ''' Calculate the exterior angle (in radians) between itself 
            and another vector v. '''
        return math.pi - self.ang(v)
    
    def area(self, v):
        ''' Calculate the area spanned by itself and another vector v. 
            Formula: S = 1/2 ab sinC. '''
        return self.normProd(v) * math.sin(self.ang(v)) / 2