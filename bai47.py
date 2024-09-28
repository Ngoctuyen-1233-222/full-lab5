# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:45:45 2024

@author: tran9
"""

#bai47
a=[]
max_t=0
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,104):
            if 2*x+7*y+9*z==979:
                tong= x+y+z
                if tong > max_t:
                    max_t=tong
                    a=[x+y+z]
if a:
    print("bo nghiem lon nhat{x,y,z}",a)
    print("tong=",max_t)
                    
