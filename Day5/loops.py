"""
For Loop
"""
list1= ["pizza", "burger", "cake"]

print(list1)
print(list1[0], list1[1], list1[2])
for items in list1:
    print(items)

item = [1,12,4,40,"smile", "python", int, float]

for items in item:
    if str(items).isnumeric()and items>6:
        print(items)

"""
While Loop
"""

i=0
while(i<45):
    print(i, end=" ")
    i=i+1


i=0
while(True):
    if i<5:
        i=i+1
        continue
    print(i, end=" ")
    if (i==44):
        break
    i=i+1


i=0
while(True):
    if i<100:
        i=i+1
        continue
    print("You have reached 100")
    break;


while(True):
    num = int(input())
    if num>100:
        break
    else:
        continue
    
    






