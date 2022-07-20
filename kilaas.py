# def greet():
    # print("Hello,world!")
    # return 'Hi Mars!'


# def factorial(n):
#     fact = 1
#     for i in range(1 , n+1):
#         fact = fact * i
#     return fact


# fact_of_5= factorial(5)
# fact_of_10 = factorial(10)

# print(fact_of_5)
# print(fact_of_10)


# def table(n):
#          for i in range(1 , 11):
#             print(n*i)
            
# table(12)
# table(5)

# info = []
# def list():
#         for i in range(0,3):
#             element = input("Enter an elemnet")
#             info.append(element)
#         return info
# data = list()
# print(data) 

        
# def capital():
#     e1 = input("Enter a value")
#     if e1.isupper():
#             return True
#     else :
#             return False
# cap = capital()
# print(cap)

# def sum_of_ascii(string):
#     total = 0
#     for i in string:
#         total = total +ord(i)
#     return total
# c = sum_of_ascii('khags')
# print(c)


# def sum_of_uname_pass(username,password):
#     val = username[0:4] + password[-4:]
#     return val
# sum_ = sum_of_uname_pass('Divyansh','12nhdje')
# print(sum_) 


def count_next_char(input_string):
    total = 0
    for i in range(len(input_string))-1:
        if input_string[i] == input_string[i+1]:
                total += 1
    return total