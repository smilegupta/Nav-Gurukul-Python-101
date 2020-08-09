'''
Day1:

1. Introduction to Python
2. Basic character types

'''

hey = 1
hey1 = "krutika"
hey2 = "d"

print(hey, hey1, hey2)


ccd = "I am good"
f = " "
de = "krutika"

print(ccd +f+ de)


x = 50
y = 10

# Addition of variables 
d = x + y
e = x * y
f = x - y
g = int(x / y)

print(d,e,f,g)

x = 5
y = 20

# Power of variables ex. 3 ^ 2 = 9

ans = x ** y
print(ans)


x = 2
y =3

x == y

'''
1. Arithmetic Operators ( x + y, x//y, t//y)
2. Assignment Operators ( x = 2, x = x + 3, x = x**3, x = x <<3 )
3 Comparison Operators ( x == y, x>=y, x <=y)
4. Logical Operators ( x<y and x == y)
5. Identity Operators (is, is not)
6. Membership Operators (in, not in)
7. Bitwise Operators (&, |, <<, >>, ^)
'''


x = 5
y = 2
print(x % y)

'''
Sample Question:

1. Add the value of x and y store it in z
2. Multiply z with k store the value in r.
3  Find the value of square of r and store in p
4. Print the value of p
'''

x = 40 
y = 10
k =3

z = x + y
r = z * k
p = r ** 2
print(p)

'''
Sample Question: 

Make two strings
1. Laptop
2. Education

The output should be 
"Laptop Education" 
"LaptopEducation"
'''

a = "Laptop"
b = "Education"

e = " "

print(a+e+b+"\n",a+b)
'''
x = 30
y = 10

# Conversion to different data types
a = x/y
b = str(x/y)
c = int(x/y)

print(a, b, c)
