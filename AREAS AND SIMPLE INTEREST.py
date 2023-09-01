#Python Code To Find The Area Of Circle By Bello O.A

print("===========Area Of Circle========")

radius = float(input("Enter radius of circle = "))
Area = 3.142*(radius*radius)
print("Area of Circle:", (Area))


#Python Code To Find Simple Interest By Bello O.A

print("=====+++++====Simple Interest++++======++++")

P = int(input("Please enter the principal = "))
R = float(input("Please enter the rate = "))
T = float(input("Please enter duration period = "))
SI= (P*R*T)/100
print("Simple Interest:", (SI))


#Python Code To Find Area Of Triangle In Three Different Ways

print("=======Area Of Triangle (First Method)======")

Base = float(input("Enter the base of the triangle = "))
Height = float(input("Enter the Height of the triangle = "))
Area = 0.5*Base*Height

print("Area of Trianlge:", (Area))


print("=======Area Of Triangle (HERON's FORMULAR)=======")
import math
math.sqrt
a = int(input("Enter the first side = "))
b = int(input("Enter the second side = "))
c = int(input("Enter the third side = "))
S = (a+b+c)/2
A = math.sqrt(S*(S-a)*(S-b)*(S-c))
print(S)
print("Area of Circle:",(A))
