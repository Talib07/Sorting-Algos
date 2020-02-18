# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:28:29 2019

@author: Talib
"""
class daynames:
    def __init__(self,names=None):
        self.names = names
        self.next = None
        
ob1 = daynames("Mon")
ob2 = daynames("Tue")
ob3 = daynames("Wed")
ob4 = daynames("Thur")
ob5 = daynames("Fri")

ob1.next = ob2
ob2.next = ob3
ob3.next = ob4
ob4.next = ob5

thisvalue = ob1

while thisvalue:
    print(thisvalue.names)

        
        