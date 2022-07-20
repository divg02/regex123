# a= input("input a number: ")
# b= input("enter another number: ")

# operation= input("type the operation you want to perform: ")
# if operation == "+":
#     print(a+b)
# elif operation == "-":
#     print(a-b)
# elif operation == "*":
#     print(a*b)
# elif operation == "/":
#     print(a/b)
# elif operation == "%":
#     print(a%b)

# n = input("enter a number :")
# list = n.split()

# if list[0] == 'add':
#     add_=0
#     for i in range(1,len(list)):
#         add_+= int(list[i])
#     print(add_)
       
# elif list[0] == 'mult':
#     mult_=1
#     for i in range(1,len(list)):
#         mult_*= int(list[i])
#     print(mult_) 

# a =  int(input("Enter the number you want factorial of: "))
# for i  in range(1,a):
#     a = a*i
# print(a)

# x = (input())
# s = str(x)
# rs = s[::-1]
# if s==rs:
#     print('yes')
    
# else: 
#     print('no')

n = int(input("Enter number of character: "))
str_= ""
for i in range( n):
    x = int(input(f"enter {i + 1} character: "))
    str_+=(chr(x))
print(str_)

