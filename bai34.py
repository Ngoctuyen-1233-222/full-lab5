# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:40:29 2024

@author: tran9
"""

#bai34
n=int(input("nhap vao so nguyen N:"))
while n<=0:
    n=int(input("nhap lai so nguyen N:"))
if n<=2:
    print("day khong phai so nguyen to:")
else:
    for i in range(2,n+1):
        if n%1 ==0:
            print("day kh phai so nguyen to:")
            break
    else:
          print("day la so nguyen to:")