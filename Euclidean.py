# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:28:57 2016

@author: ceciliaLee
"""

u = (3, 0)
v = (0, 4)


def euclidean(u, v):
    """Returns the Euclidean distance between points u and v."""
    return ((v[0] - u[0])**2 + (v[1] - u[1])**2)**0.5

print euclidean(u, v)