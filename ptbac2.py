# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:27:17 2024

@author: Le Pham Nhu Y
"""

import math
a= float(input("Nhập a:"))
b= float(input("Nhập b:"))
c= float(input("Nhập c:"))
delta= b**2-(4*a*c) 
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    print("Phương trình có nghiệm kép X1=X2",-b/2*a)
else: 
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Phương trình có 2 nghiệm phân biệt X1",x1)
    print("Phương trình có 2 nghiệm phân biệt X2",x2)
    
