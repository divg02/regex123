
lst = [1,2,3,4,5,5,6,7,8,9] 

# for i in lst[2:]:
#     print(i)

# print(range(10))

# for x in lst[:5]:
#     print(x)

 
# for i in 'hello':
#     print(i)

for i in range(0,len(lst),2):
 print(lst[i])

# for i in [1,2,3]:
#     for j in ['a','b','c']:
#         print(i,j)


# prime number 
flag = 0
print(type(flag))
i = int(input("enter number "))
l = int(i/2)
for x in range(2,l): 
    if((i%x)==0):
        flag=1
        break
    

# if(flag==1):
#     print("not prime number")
    

# else:
#     print("prime number")

# i=0
# while i < 5:
#     print(i)
#     i +=1
    