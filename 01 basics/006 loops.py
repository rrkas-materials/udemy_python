#------------FOR In LIST------------------------------------------------
# temps = [9.1 , 8.8, 7.6]

# for t in temps:
#     print(round(t))

# for l in 'hello':
#     print(l.upper())

#-------------FOR In DICT----------------------------------------

# mydict = {"a":1,"b":2,"c":3}

# for a in mydict.items():
#     print(a)

# for a in mydict.keys():
#     print(a)

# for a in mydict.values():
#     print(a)

#-----------WHILE LOOP------------------------------------------

# a = 10
# while a>0:
#     print(a)
#     a=a-1

#---------BREAK AND CONTINUE-----------------------------------------------------

while True:
    user = input("Enter name: ")
    if user == 'break':
        break
    elif user == 'skip':
        continue
    print(user)