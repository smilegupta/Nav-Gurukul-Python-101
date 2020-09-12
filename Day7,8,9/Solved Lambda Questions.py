# Lambda Practice Questions
"""
1) Write a Python program to extract year, month, date and time using Lambda.

2) Create a lambda function that adds 15 to a given number passed in as an argument

3) Removes the positive numbers from a given list of numbers 
and Sum the negative numbers and 
print the absolute value using lambda function


import datetime
now = datetime.datetime.now() 
year = lambda x: x.year
print(year(now))
day = lambda x:x.day
print(day(now))

number = lambda a:a+15
print(number(100))

"""

nums=[2, 4, -1, -2 ]


print(abs(sum([i for i in nums if i < 0])))



"""
import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now)) 



r = lambda a : a + 15
print(r(10))



nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list: ", nums)
print("Result:")
print(abs(sum([i for i in nums if i < 0]))) 


"""