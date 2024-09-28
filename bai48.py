# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:51:54 2024

@author: tran9
"""

a=[]
min_t=999
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,104):
            if 2*x+7*y+9*z==979:
                tong=x+y+z
                if tong < min_t:
                    tong= min_t
                    a=[{x,y,z}]
if a:
    print("bo nghiem nho nhat",a)
    print("tong=",min_t)
