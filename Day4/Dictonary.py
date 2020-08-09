Dict={"mutable":"can change" , "immutable":"Can't Change"}
name=input("Enter the name ")
key=name.capitalize()
print(key, " = ",Dict[name.lower()])
