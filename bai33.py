# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:34:46 2024

@author: tran9
"""

#bai33
import math
n=int(input("nhap vao so nguyen N:"))
sochinhphuong= math.sqrt(n)
a=int(sochinhphuong)
tong=a*a
if n==tong:
    print("day la so chinh phuong:")
else:
    print("day kh phai so chinh pphuong:")
    
