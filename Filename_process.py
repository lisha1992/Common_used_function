# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:22:01 2016

@author: ceciliaLee
"""

###### Split the filename into 2 parts: name and its suffix
from os.path import splitext
def remove_ext(filename):
    base, _ = splitext(filename)
    return base ## return filenames without  ".txt" but with filepath
# base=remove_ext("data/arabian_nights/1.txt") 
## removes the directory from a filepath.
    
from os.path import basename
def remove_dir(filepath):
    return basename(filepath) ## return the complete filenmaes without directions(filepath)
# remove_dir("data/arabian_nights/1.txt")  
    
# Combine the two functions remove_ext and remove_dir
# takes as argument a filepath and returns the name (without the extensions) of the file
def get_filename(filepath):
    return remove_dir(remove_ext(filepath))
# get_filename("data/arabian_nights/1.txt") # return 1