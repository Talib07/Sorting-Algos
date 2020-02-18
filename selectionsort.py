# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:20:20 2019

@author: Talib
"""

def selectionsort(a):
    n = len(a)
    i = 0
    while((n-i)>=2):
        k = min(a[i:n])
        swap(a,i,a.index(k))
        i+=1
    return a
        
         
def swap(a,x,y):
    a[x],a[y] = a[y],a[x]
    return a