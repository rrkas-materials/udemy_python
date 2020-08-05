# def getTemp(temp):
#     if temp>7:
#         return 'Hot'
#     else:
#         return 'Cold'

# t = float(input("Enter Temperature: "))
# print(getTemp(t))

#----------------------------------------------------------------------
#STRING FORMATTING

# inp = input("Enter your name: ")
# message = "Hello %s!" % inp
# #or
# message = f'Hello {inp}'
# print(message)

name = input("Enter name: ")
surname = input("Enter surname: ")
age = float(input("Enter age: "))
message = 'Hello %s %s. You\'re %s years old!' % (name, surname, age)
#or
message = f'Hello {name} {surname}. You\'re {age} years old!'
print(message)



'''
%s : variable, unlike %s for only strings in C 

'''
