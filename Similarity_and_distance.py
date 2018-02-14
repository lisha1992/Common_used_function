#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:05:22 2018

@author: ceciliaLee

Similarity and distance calculation
"""

import numpy as np


def L1Dist(A, B):
    """
    L1 Distance
    A, B: type = np.asarray()
    """
    return np.sum(np.abs(A - B))

def L2Dist(A, B):
    """
    Euclidean Distance
    L2 Distance
    A, B: type = np.asarray()
    """
    return np.sqrt(np.sum((A - B) ** 2))

def ChiSquareDist(A, B):
    """
    Chi-Square Distance
    """
    return np.sum(np.where(A > 0, ((A - B) ** 2) / A, 0))

def KLDist(A, B):
    """
    KL Distance
    """
    return np.sum(np.where(B != 0, A * np.log(A / B), 0))


def CosineSimilarity(A, B):
    """
    Function for calculating cosine similarity between two image
     
    """
    numerator = (A * B).sum()
    denoma = (A * A).sum()
    denomb = (B * B).sum()
    return 1 - numerator / np.sqrt(denoma*denomb)

def hist_intersection(A, B):
    """
    Function for calculating histogram intersection between two image

    """
    min_matrix = np.where(A >= B, B, 0) + np.where(A < B, A, 0)
    the_min = min_matrix / float(min(np.sum(A.ravel()), np.sum(B.ravel())))
    return sum(the_min.ravel())
