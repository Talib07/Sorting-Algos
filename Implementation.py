# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:33:25 2019

@author: Talib
"""
class Node:
    def __init__(self,names=None):
        self.names = names
        self.next = None
        
class LinkedLists:
    def __init__(self):
        self.head = None
        
    def Print(self):
        printval = self.head
        while printval is not None:
            print(printval.names)
            printval = printval.next
                
ob1 = LinkedLists()
ob1.head = Node("Mon")
ob2 = Node("Tue")
ob3 = Node("Wed")
ob4 = Node("Thur")
ob5 = Node("Fri")

ob1.head.next = ob2
ob2.next = ob3
ob3.next = ob4
ob4.next = ob5
   
ob1.Print()