# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:37:48 2024

@author: tran9
"""
#bai 46
ds=[]
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,104):
            if 2*x+7*y+9*z==979:
                if 2*x+7*y+9*z==979:
                    tong=(x+y+z)
                    ds=[{x,y,z}]
if ds:
    print(f"{ds}")
