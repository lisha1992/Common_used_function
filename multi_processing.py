#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:47:56 2017

@author: ceciliaLee
"""

import multiprocessing as mp
import threading as td

def job(q,num): 
    ## no return is allowed, put results into Queue q, q should be the input parameter
    
    res = []
    for i in num:
        res.append(i*2)
    q.put(res)

def job_pool(x):
    return x**x
def test(x):
    print [i*2 for i in x]
    print 'test_1_1_done.\n'
   
    print [i*10 for i in x]
    print 'test_1_2_done.\n'
    
def test2(x):
    print [i*0.1 for i in x]
    print 'test_2_1_done.\n'
    print [i*100 for i in x]
    print 'test_2_2_done.\n'
  
def test3(arr1, arr2):
    counts = []
    for i in arr1:
        d ={}
        for j in arr2:
            d.setdefault(j, 0)
        for k in i:
            if k in arr2:
                d[k]+=1
        counts.append(d)  
    return counts
    

    
def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(100))
    print res
    res = pool.apply_async(job, (2, ))
    print res.get()
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    print [res1.get() for res1 in multi_res]



    
if __name__=='__main__':
    """"
    x = [0,1,2,3,4,5,6,7,8,9]
    p1 = mp.Process(target=test, args=(x,))
    p2 = mp.Process(target=test2, args=(x,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    """
    pool = mp.Pool()
    arr2 = ['a','b','c','d']
    arr1 = [
            ['a','a'],
            ['a','e'],
            ['a','b'],
            ['b','c'],
            ['b','e'],
            ['a','b','c','d'],
            ['1','2','3']
            ]
    res = pool.apply_async(test3,(arr1,arr2)) 
    print res.get()
    
    
    


    
    

