# Function Practice Questions
"""

1)  Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]


2) Write a Python function that checks whether a passed string is palindrome or not. 
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, 
e.g., madam or nurses run.

3)  Write a Python function to create and print a list where the values are square of
numbers between 1 and 30 (both included).

4)  Write a Python function that accepts a string and calculate the number of upper
     case letters and lower case letters.

5) Write a Python program to reverse a string.

6) Write a Python function to sum all the numbers in a list.


7) Write a Python program
     that accepts a dash-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow


jyoti-pranjali-mehak-suman-gouri

step1:  thodna (split) >>>  jyoti pranjali mehak suman gouri  .split 
step2: sorting >>> gouri jyoti mehak pranjali suman .sort
step3: adding hyphen/dash again .join

def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')

def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))

def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza')) 


def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)
		
printValues()

"""
"""

lambda a: a+b

a for n in list1




list = ["hello-smile"]

for i in list:

"""
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 = rstr1 + str1[ index - 1 ]
        index = index - 1
    return rstr1

print(string_reverse('axe'))
string1="classmate"
print(string1[len(string1):0:-1])


"""
a =  axe
     012
     
a[1:]+a[0] xea
a[1:] = xe


 
"""