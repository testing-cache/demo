print("hello")
print("this is 1st time")

a=100
b=1.5
c=a+b
print(type(c))

num=5+2.0
print(num)

num_int=int(5.7)

print(num_int)

num_float=float("3.14")
print(num_float)

message=str(42)
print(message)

is_true=bool(1)
print(is_true)

is_false=bool(0)
print(is_false)

# d="john"
# print(int(d))


char_a="A"
print(ord(char_a))

charz="Z"
print(ord(charz))

g=65
print(chr(g))



#Floor DIVISION

i=10
j=3
print(i/j) #normal division
print(i//j) #floor division

#remainder

K=10
L=3
print(K%L)


#exponentiation
m=2
n=3
print(m**n)

#Assignment operators

a=10
b=20
print(a)
print(b)
a=a+b
print(a)
     #or
a+=b
print(a)

a=10
b=20
a-=b
print(a)

a=10
b=20
a*=b
print(a)

a=10
b=20
a/=b
print(a)

a=2
b=2
a/=b
print(a)

a=2
b=2
a//=b
print(a)

a=2
b=2
a%=b
print(a)

a=2
b=2
a**=b
print(a)


#and
a=True
b=False
print(a and b)       #False

#or

a=True
b=False
print(a or b)


#membership operator
t=[1,2,3]
print(1 in t)
print(10 not in t)

fruits=["apple","banana","cherry"]
print("apple" in fruits)
print("jackfruit" not in fruits)