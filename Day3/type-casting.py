"""
Basics of typecasting
str()
int()
float()
"""

var1="Hello World"
var2=4
var3=36.7
var4="4"
var5="36.7"
#print(type(var1))
#print(type(var2))
#print(type(var3))

print(var2+var3)
# print(var1+var2) -- here an error will come
print(var4+var5)
print(int(var4)+float(var5))
print(5*var2)
print(5 * (var4+"\n"))
print(5*(str(var2)+"\n"))



