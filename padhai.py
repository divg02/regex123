# [] - List
# () - Tuple
# {} - Dictionary
# Dictionary is nothing but key value pairs
# d1 = {}
# # print(type(d1))
# d2 = {"Harry":"Burger",
#       "Rohan":"Fish",
#       "SkillF":"Roti",
#       "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
# d2["Ankit"] = "Junk Food"
# d2[420] = "Kebabs"
# print(d2)
# del d2[420]
# print(d2["Shubham"])
# print(d2["Shubham"]["B"])
# d3 = d2.copy()
# del d3["Harry"]
# d2.update({"Leena":"Toffee"})
# print(d2.keys())
# print(d2.items())


# s = set()
# # print(type(s))
# # l = [1, 2, 3, 4]
# # s_from_list = set(l)
# # print(s_from_list)
# # print(type(s_from_list))
# s.add(1)
# s.add(2)
# s.remove(2)
# s1 = {4, 6}
# print(s.isdisjoint(s1))



# var1 = 6
# var2 = 56
# var3 = int(input())
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 7, 3]
# print(15 not in list1)
# if 15 not in list1:
#     print("No its not in the list")

# # Quiz
# print("What is your age?")
# age = int(input())
# if age<18:
#     print("You cannot drive")

# elif age==18:
#     print("We will think about you")

# else:
#     print("You can drive")


# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
#

from timeit import repeat


print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print('so What you Want?'+'+,-,/,%,*')
num3 =input()

if num1 ==45 and num2==3 and num3=='*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("4")
elif num3=='*' :
    num4=num1*num2
    print(num4)
elif num3 == '+':
    plus=num2+num1
    print(plus)
elif num3 == '/':
    Dev=num2/num1
    print(Dev)
elif num3 == '-':
    Dev=num2-num1
    print(Dev)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")
    
