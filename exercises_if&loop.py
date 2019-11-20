#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:27:56 2019

@author: owner
"""

#EX1:Write a Python program to accept 2 numbers from the users and print the greatest
"""
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
if num1>num2 :
    print(num1)
else: print(num2)
"""
#Ex2:Write a Python program to create the multiplication table for a specific number that is accepted from the user
"""
num1=int(input("Enter Number:"))
i=1
while i<=10 :
    print(num1,"*",i," =",num1*i)
    i+=1
"""
#EX3:Write a Python program to construct the following pattern, using a nested for loop.
"""
number=9
for row in range(number):
    for col in range(row):
        print("* ",end="")
    print()
for col in range(number, -1, -1):
           for row in range(0, col + 1):
               print("* ", end="")
           print()
"""
#EX4:WHAT OUTPUT
"""
letters=["x","y","z","a","b","c"]
for i in letters:
    if i == 'a':
        continue
    elif i == 'c':
        break
    print(i)
"""
#EX5:OUTPUT:
"""
for x in range(12,25,3):
    print(x)
"""
#EX6:OUTPUT:
"""
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

    """
#EX7:SUM ALL the number between 0 and the number
"""
num=int(input("Enter number:"))
i=1
while i <= num :
    print(num,"+",i,"=",num+i)
    i+=1
"""    
#EX8:Odd&even
"""
num=int(input("Enter number:"))
if (num % 2) == 0:
    print("even")
else: print("odd")
"""
#EX9:

for i in range(1,10): 
    for j in range(10-i):
        print(" ",end=" ")
    for j in range(1,i):
       print(j,end=" ")
    for i in range(i,0,-1):
        print(i,end=" ")
    print()    
for i in range(8,0 , -1):
   for j in range(10 - i):
       print (" " , end=" ")
   for j in range(1,i):
       print(j, end=" ")
   for i in range(i , 0 , -1):
       print(i , end=" ")
   print()
#EX10:
"""
while True:
 try:
   n = input("Please enter an integer: ")
   n = int(n)
   break
 except ValueError:
   print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")
"""
#EX11: OUTPUT
"""
try:
 a=3
 if a<4 :
    b=a/(a-3)
 print("value of b=",b)
except(ZeroDivisionError,NameError):
    print("\nError Occurred and Handled")
"""

         
             