# Indian Kirana Store Generator

print("Welcome to Shudh Desi General Store!")
print("We hope you have an amazing day!")
print("Before you start your shopping, please enter the following details")
name=input("Your good name please ")
number=int(input("Please enter your mobile number "))
address=input("Please give details of your address ")
item_name= []
item_quanity=[]
item_price=[]
sum = 0
while(True):
    userInput=input("Press c to continue! else press any key to generate bill \n")
    if(userInput == 'c'):
        product=input("Enter the name of product ")
        item_name.append(product)
        quantity=int(input("Enter the quanity "))
        item_quanity.append(quantity)
        price=int(input("Enter price per single item "))
        item_price.append(price)
        sum=sum+(quantity*price)
    else:
        print("**********Shudh Desi General Store**********")
        print("***Main GT Road Mullanpur Mandi, Ludhiana***")
        print("Customer Name: ", name)
        print(address)
        print("Mobile Number: ", number)
        size= len(item_name)
        i = 0
        print("**********Shudh Desi General Store**********")
        print("Total Items Bought: ", size)
        print("Here is the summary list")
        while(i<size):
            print("Item Number: ",i+1)
            print("Name of Item: ",item_name[i])
            print("Quantity : ",item_quanity[i])
            print("Price per Item: ",item_price[i])
            i=i+1
        
        print("Total bill of yours is Rs. ",sum)
        print("Thankyou for shopping with us")
        break
    
    
    

