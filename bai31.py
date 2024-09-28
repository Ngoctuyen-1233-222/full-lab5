# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:08:11 2024

@author: tran9
"""

#bai31
a=int(input("nhap he so nguyen a:"))
b=int(input("nhap he so nguyen b:"))
c=int(input("nhap he so nguyen c:"))
if a+b>c and a+c>b and c+b>a:
    if a==b==c:
        print("day la tam giac deu:")
    elif a==b!=c and a==c!=b and c==b!=a:
        print("day la tam can:")
    elif a**2+b**2==c**2 and a**2+c**2==b**2 and c**2+b**2==a**2:
        print("day la tam giac vuong:")
    else:
        print("con lai la tam giac thuong:")
else:
    print("con lai khong phai tam giac:")
    
        
        
    print("day la tam giac vuong:")
    ee

    
    
    
    
            