"""
Dictory is the collection of key and value pair
"""
d1={}
# print(type(d1))
d2={"Smile":"Python",
    "Shivanshu":"Java"}
print(d2)
d2["Prachi"]="HTML"
d2.update({"Shaina":"Clients"})
print(d2)
del d2["Shivanshu"]
print(d2)
print(d2.keys())
print(d2.items())
print(d2.values())
