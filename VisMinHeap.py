# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 15:40:01 2016

@author: Bluefish_
A minimum heap (priority queue) for Visvalingam algorithm.

"""

class min_heap:
    """ A min priority queue for areas implemented with a binary heap. """
    
    def _parent(self, index):
        ''' Return the index of the parent of a given item. '''
        return (index - 1) // 2
    
    def _left(self, index):
        ''' Return the index of the left child of a given item. '''
        return 2 * index + 1
    
    def _right(self, index):
        ''' Return the index of the right child of a given item. '''
        return 2 * index + 2
    
    def _has_left(self, index):
        ''' Return true if the given item has a left child. '''
        return self._left(index) < len(self._data)
    
    def _has_right(self, index):
        ''' Return true if the given item has a right child. '''
        return self._right(index) < len(self._data)
    
    def _swap(self, i, j):
        ''' Swap two nodes at index i and j. '''
        self._data[i], self._data[j] = self._data[j], self._data[i]
        
    def _bubbleUp(self, child):
        ''' Bubble up / Swim. '''
        parent = self._parent(child)
        if (child > 0) and (self._data[child] < self._data[parent]):
            self._swap(child, parent)
            self._bubbleUp(parent) # do the bubbling recursively
    
    def _bubbleDown(self, parent):
        ''' Bubble down / Sink. '''
        if self._has_left(parent):
            left = self._left(parent)
            smaller = left # smaller refers to the node where we bubble down
            if self._has_right(parent):
                right = self._right(parent)
                if self._data[smaller] > self._data[right]:
                    smaller = right
            if self._data[smaller] < self._data[parent]:
                self._swap(smaller, parent)
                self._bubbleDown(smaller) # do the bubbling recursively
    
    # - the above are node-related operations
    # - the following are heap-related operations
    
    def __init__(self):
        ''' Initializa the empty list. '''
        self._data = []
    
    def __len__(self):
        ''' Return the number of items in the heap. '''
        return len(self._data)
    
    def is_empty(self):
        ''' Return true if the heap is empty. '''
        return len(self) == 0    
    
    def push(self, tri):
        ''' Insert a point into the heap. '''
        self._data.append(tri)
        self._bubbleUp(len(self._data)-1) # bubble the node up the heap
    
    def min_area(self):
        ''' Return the item with the smallest area. '''
        if self.is_empty():
            print("The heap is empty. ")
        item = self._data[0]
        return (item._id, item._t) # return the id and the triangle
    
    def remove_min_area(self):
        ''' Remove the item with the smallest area and return this item. '''
        if self.is_empty():
            print("The heap is empty. ")
        self._swap(0, len(self._data)-1) # put the minimum value at the end
        item = self._data.pop()
        self._bubbleDown(0) # bubble from the root down to a suitable place
        return item # return the whole item
    
    def remove(self, item):
        ''' Remove a certain item from the heap. '''
        return self._data.remove(item)
    
    def to_list(self):
        ''' Return the data in the heap. '''
        return self._data