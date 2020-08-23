# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:57:34 2020

@author: Smile Gupta
"""


# Basic Function without Argunment
def welcome():
    print("Happy Learning")
    
welcome()


# Basic Function with Argunment

def add(a,b):
    """This function does not run for three number"""
    total=a+b
    print(total)

print(add.__doc__)
add(5,6)

#Function with Argunments
def add2(a=0,b=0):
    total=a+b
    print(total)
add2(5)
add(b=10,a=10)

# Passing List as a Argunment
def add4(*num):
    total=0
    for i in num:
        total=total+i
    print(total)
        
add4(10,20,30,40,50)


#Using return in Functions

def add5(a=0, b=0):
    total = 0
    total=a+b
    return total
ans=add5(10,100)
print(ans)


# Lambda Expressions

fun = lambda a,b:a+b
print(fun(10,20))
        