# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:57:01 2024

@author: tran9
"""

#bai30
a=int(input("nhap thang"))
b=int(input("nhap nam"))
if b%4==0 and b%400==0 and b%100==0:
    print("nam nay la nam nhuan:")
if a==2:
    print("thang nay co 29 ngay:")
else:
    print("nam nay la nam nhuan:")
    if a==2:
        print("nam nay khong phai nam nhuan:")
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("thang nay co 31 ngay:")
if a==4 or a==6 or a==9 or a==11:
    print("thang nay co 30 ngay:")

