# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:14:16 2024

@author: Le Pham Nhu Y
"""
a= float(input("Nhập a:"))
b= float(input("Nhập b:"))
c= float(input("Nhập c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c: 
        print("3 cạnh tạo thành tam giác đều")
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2: 
        print("3 cạnh tạo thành tam giác vuông") 
    elif a==b or a==c or b==c: 
        print("3 cạnh tạo thành tam giác cân") 
else: 
    print("3 cạnh tam giác thường")
            
            