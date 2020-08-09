"""
String: Stream of Characters 
        jo hum '' ya "" mei likhte hai

        Index Starts with 0

        2 Operations hote hai espe
            repetation (*)
            concatenation (+)
        Slicing
"""
mystr="We are learning Python"
print(mystr)
#Mujhe eske length print krne hai
print(len(mystr))
# Mujhe eska kuch tukda print krwana hai -- Slicing 
print(5)
print(mystr[0:3])
# print(mystr[78]) -- yeh error de ga
print(mystr[0:78])
print(mystr[-4:-2])
print(mystr[:])
print(mystr[0:])
print(mystr[:5])
print(mystr[0:5:])
print(mystr[0:5:-1])

# Commonly used String Functions
print(type(mystr))
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("python"))
print(mystr.count("o"))
mystr.capitalize()
print(mystr)
mystr.lower()
print(mystr)
mystr.upper()
print(mystr)
print(mystr.replace("are", "were"))





