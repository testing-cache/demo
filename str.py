# str="PYTHON"
# print(str)
# print(str[0])
# print(str[-1])


####string slicing



st1="HELLO WORLD"
print(st1[1])
print(st1[-1])
print(st1[1:3]) ##h-0e-1l-2l-3o-4 5 w-6o-7r-8l-9d-10
#prints from index 1 to 2,but not 3 asit was stopping at 3
print(st1[1:-1]) #prints from index 1 to index -1 before d)
print(st1[:3])#prints from 0 to 3

print(st1[2:])# if no stop is gevien we can take all the character including the last character
print(st1[::2]) # prints from index 0 but skips every 2nd index hlowrd
print(st1[1::2])# prints from index 1 but excludes every 2nd index el wrd
print(str[::-1])# prints the str from the last index to 1st index dlrow olleh
