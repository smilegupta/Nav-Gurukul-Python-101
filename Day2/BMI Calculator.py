#BMI Cal  or शरीर द्रव्यमान सूचकांक
# weight / (height * height)
# BMI < 18.5 (Under Weight) 18.5- 24.9 (Healthy).
# 24.9 > Unhealthy
# 1 pound = 0.4535kg
# 1 inch = 0.254 meters

pound = 0.4535
inch = 0.254
name = input("Enter your name")
weight = float(input("Enter your Weight in Pound"))
height = float(input("Enter your Height in inches"))

weight = weight*pound
height = height*inch
ans = weight/ (height * height)

print("Hey! ", name, "your BMI score is ", ans)

