# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:37:53 2020

@author: DELL

"""

# Reading File

f =  open("sample.txt", "r")
content = f.read()
# content = f.read(3)  --- To read first three characters 
# other functions 
print(content)
f.close()


# Writing a file 

f = open("sample2.txt" , "w")
f.write("Smile Loves Dog")
f.close()



# Read and Writing a file 

f =  open("sample2.txt", "r+")
print(f.read())
f.write("\n thankyou")
f.close()
