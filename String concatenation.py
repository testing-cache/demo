# # # # # first_name="ram"
# # # # # last_name="bollepalli"
# # # # # full_name=first_name + " " + last_name
# # # # # print(full_name)
# # # # # print(len(full_name))#to print the length of the string

# # # # s="HEllo World"
# # # # print(s.upper())
# # # # print(s.lower())
# # # # # print(s.strip)
# # # # print(s.replace('H','R'))
# # # # print('abracadabra'.count('a'))


# # # # vowel counter
# # # # aeiou
# # # # outpu number of vowels :

# # # # s=input("enter the string : ")
# # # # s=s.lower()
# # # # a = s.count("a")
# # # # e = s.count("e")
# # # # i = s.count("i")
# # # # o = s.count("o")
# # # # u = s.count("u")
# # # # print(f"number of vowels in the string are : {a+e+i+o+u}")


# # # #grade calculator:
# # # #input marks in math:85
# # # #marks in science:90
# # # #marks in english:95
# # # #output total marks:
# # # #average marks:
# # # #grade
# # # math=int(input("enter the marks in Math : "))
# # # science=int(input("enter the marks in Science : "))
# # # english=int(input("enter the marks in English : "))
# # # grade=(math+science+english)/300*100
# # # print(f"Total marks: {math+science+english}")
# # # print(f"Average Marks: {(math+science+english)/3}")

# # # if grade >90:
# # #     print("A+")
# # # elif grade >80 and grade <=90:
# # #     print("B")
# # # elif grade >70 and grade <=80:
# # #     print("C")
# # # elif grade >60 and grade <=70:
# # #     print("D")
# # # elif grade >50 and grade <=60:
# # #     print("E")
# # # elif grade <=50:
# # #     print("F")


# # #palindrome:
# # #input "radar"
# # #output it is a palindrome

# # pal=input("enter the string : ")
# # palindrome=pal[::-1]
# # if palindrome==pal:
# #     print(f"{pal} is a palindrome")
# # else:
# #     print("not a palindrome")


# #largest of three number
# #input enter three numbers
# #output largest number is 
# a,b,c=input("enter the numbers : ").split(",")
# a=int(a)
# b=int(b)
# c=int(c)
# if a>b and a>c:
#     print(f"the largest number is {a}")
# elif b>a and b>c:
#     print(f"the largest number is {b}")
# elif c>a and c>b:
#     print(f"the largest number is {c}")

#leapyear
#divisbile by 4,not divisbile by 100,divisible by 400
year=int(input("enter the year : "))
if year%4==0:
    if year%100 !=0 or year%400==0:
        print(f"{year} is a leap year")