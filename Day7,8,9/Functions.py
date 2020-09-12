


# Basic Function without Argunment
def welcome():
    print("Happy Learning")
    
welcome()


# Basic Function with Argunment

def add(a,b):
    
    total=a+b
    print(total)

#print(add.__doc__)
print(sum.__doc__)
# add(5,6)

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
