"""
Mutable: Can Change -- List
Inmutable: Can't Change -- Tuple

"""

Grocery=["Harpic", "VimBar", "Bhindi", "Lays"]
print(Grocery)
print(Grocery[0])

numbers = [2,7,9,11,3]
print(numbers)
print(numbers[2])
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))

numbers.insert(1,67) # Adding number at specific position
print(numbers)
numbers.append(9)
print(numbers)
numbers.remove(9)# In order to delete the number itself
print(numbers)
numbers.pop() # In order to remove element from last position
print(numbers)
numbers.pop(2) # To delete from a specific index


tp=(1,2,3)
tp1=(1,) # The way to create a single element tuple
# All the functions that can we performed on list,
# Same can be performed on tuple. 
