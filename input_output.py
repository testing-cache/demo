# name=input("enter your name :")
# print(name)
# print("my name is",name)


# #
# nam1=input("enter number")
# print("my number is",nam1)

# num2=input("enter number")
# print(int(num2))

# demo = input("Enter your name: ")
# age = int(input("Enter your age: "))
# # print("hello" + demo + "my age is ", age, "yes")
# print("hello my name is " + demo + "and my age is ", age, "yes", age, demo )

# demo1=int(input("enter number"))
# print(type(demo1))
# print(demo1)

# #OUTPUT-- statement

# a=int(input("enter a value : "))
# b=int(input("enter b value : "))
# print(a,b)
# print(a,b,sep=" used & to provide the gap ")
# print(a,b, sep=",",end="   using end to dispaly eneded here")

# #Hello, John!
# ex=input("enter the expected input : ")
# print("Hello",ex,sep=",",end="!") 




# number=input("enter the number : ")
# print(type(number)) #to converto int type from str we can use below 2 types
# #  number2=int(number)
# # print(int(number))
# print(type((int(number))))

# #example 2
# #input=5
# #output you entered: 5

# num=int(input("enter the number : "))
# print("You entered:",num,sep="" )

# 3xample3
# input=3.14
# output="Value of pi:3.14"

# num=float(input("enter the number :"))
# print("Value of pi:",num,sep="")

# example4:
# input 10,20,30
# output sum of inputs: 60

# num1=int(input("enter the num1 :"))
# num2=int(input("enter the num2 :"))
# num3=int(input("enter the num3 :"))
# print("Sum of Inputs:",num1+num2+num3,sep="")


# a=input()
# x,y,z=a.split(" ")
# print("Sum of Inputs:",int(x)+int(y)+int(z),sep="")


# #exap,el 5 
# input John,25
# expected output: "Name:john,age:25"

# inp=input("enter name and age")
# name,age=inp.split(",")
# print("Name:",name,",Age:",age,sep="")

# example6
# input 5
# output Countdown:5 4 3 2 1 Blast Off!

# num=int(input("enter number"))
# print("Countdown:",num,num-1,num-2,num-3,num-4 ,end="Blast Off!",sep=" ")

# example7
# input 10,5
# output : Addition15,subtraction:5,
# Multiplication:50,Division:2.0

# num=(input("enter numbers : "))
# a,b=num.split(",")
# print("Addition:",int(a)+int(b),"Subtraction:",int(a)-int(b),"Multiplication:",int(a)*int(b),"Division:",int(a)/int(b),sep="")

# example 8
# input 10,5
# output 10>5:True,10<5:False,10==5:False,10!=5:True

# a,b=input("enter numbers : ").split(",")
# print("10>5",int(a)>int(b),"10>5",int(a)<int(b),"10>5",int(a)==int(b),"10>5","10>5",int(a)!=int(b),sep=":")

# logical operator
# input true,false
# output: true and false:False,true or false:True,not true:False

# # input1=input("enter True or false ")
# # input2=input("enter True or false ")
# input1,input2=input("enter true or false ").split(",")
# input1=bool(input1)
# input2=bool(input2)
# print("true and true",input1 and input2,"true and false",input1 or input2,"not true",not input1,sep=":")

# example 10
# input Yes(or yes,YES,yES)
# output You entered: Yes

# enter=input("enter yes or no : ")
# if enter=="Yes" or enter=="yes" or enter=="yES":
#     print("You entered:",enter)

#    # example 11 formated strings
# a,b=input("enter name and age").split(",")
# print(f"Name:{a},Age:{b}, years")

# a=int(input("enter a value : "))
# b=int(input("enter b value : "))
# print("Sum:",a+b)

# a,b=input("enter a and b value : ").split(",")
# a=int(a)
# b=int(b)
# # print("Sum:",a+b)
# print(f"Sum:{a+b}")

#find area of a circle
#input=5
#output=Area of circle with radius 5 is 78.5
# area=int(input("enter the radius of circle : "))
# print(f"Area of the circle:{area**2*3.14}")

#swap values

# a=int(input("enter a value : "))
# b=int(input("enter b value : "))
# a,b=b,a
# print(f"After swapping a={a},b={b}")

#converting temperature
# input celcius
#output Temperature in Fahrenheit: 
#temerature inkelvin

# c=int(input("enter temperature in celcius : "))
# f=c*(9/5)+32
# k=c+273.15
# print(f"Temeparature in Fahrenheat:{f},Temperature in Kelvin:{k}")

#currency converter

#input: amount_in_usd=100
#exchange_rate_usto-er=0.85
#output Equivalent amount in EUR:85.0

usd=int(input("enter amount in USD : "))
ex=0.85
print(f"Equivalent amount in EuR :{usd*ex}")


