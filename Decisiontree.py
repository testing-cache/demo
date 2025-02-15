# ##if statement
# w = input()
# if w == "sunny":
#     print("lets play cricket")

# ###if else
# w= input("enter w")
# if w=="sunny":
#     print("lets play cricket")
# else:
#     print("lets play with robot")
# print("coded ended")


#### if elif else
#w=snow, timeofday=night print play with snowman else play in snow
# w=input("enter the weather")
# timeofday=input("enter the time of day")
# if w=="sunny":
#     print("lets play cricket")

# elif w=="rainy" and timeofday=="day":
#     print("lets play bricks")
# elif w=="snow" and timeofday=="night":
#     print("lets play in snow with snowman ")    
# else:
#     print("lets plays with robot")


#calculator

a,b=(input("enter a,b values")).split(",")
calculate=input("enter the operation to be performed : ")

if calculate=="+":
    print(f"Addition of {a}+{b} is {a+b}")
elif calculate=="-":
    print(f"subtraction of {a}-{b}")

elif calculate=="*":
    print(f"Multipilication of {a}*{b}")
elif calculate =="/":
    print(f"Division of {a}/{b}")
else:
    print("invalid operation")
