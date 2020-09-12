# Fuctions and Lambda Questions for HW
"""

1) Write a Python function that takes a number as a parameter and check the number is prime or not

2) Write a Python function to check whether a number is in a given range

3) Write a Python function to check whether a number is perfect or not. 
According to Wikipedia : In number theory, a perfect number is a positive integer 
that is equal to the sum of its proper positive divisors, that is, the sum of its 
positive divisors excluding the number itself (also known as its aliquot sum). 
Equivalently, a perfect number is a number that is half the sum of all of its positive
divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its 
proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to 
half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

4) Write a Python program to access a function inside a function. 


5) Create a lambda function that adds 100 to a given number passed in as an argument

6) Create a lambda function to multiply two number passed in as an argument

7) Write a Lambda to sum all the numbers in a list.




Complete the code  to create a string containing a double quote?

"""
num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  
   
   
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))
 

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())



r = lambda a : a + 100
print(r(10))


r = lambda x, y : x * y
print(r(12, 4))


nums = [2, 4]
print(sum([i for i in nums]))
