#>>>>>>>>>>>>>>>>>loop<<<<<<<<<<<<<

# for i in range(10):
#     print('hello world',i)

#[starting , stoping , jump]
# for i in range(5,10):
#     print('hello world',i)

# i=0
# while(i<10):
#     print('hello world')
#     i +=1

#>>>>>>>>>>If we Know the no. of iterations
# for i in range(100):
#     print("Welcome")

# condition =True
# while condition:
#     user_input=input("Do you want to quit this program y/n")
#     if user_input=='y' or user_input=='Y':
#         condition=False
#     print("welcome to you in Upflairs")

#Break , continue
# count = 0
# for i in range(10):
#     count +=1
#     break
#     print("highhh")
# print(count)


ls=[52,41,63,96,85,7,45,86,6,9,12,36,72,11,22,33]

#is 85 present in ls,if it it present then tell the position on whic 85 is present

# if 85 in ls:
#     print('present')
# else:
#     print('not present')    

# count=0
# for item in ls:
#     if item==85:
#         print('present',count)
#         break

#     count+=1


# print('final count ',count)    

#ls min(),max()
#*
# **
# ***
# ****
# *****
# ******

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
       print(j,end="")
    print()