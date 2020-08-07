# my terminal is at root folder, same level as .gitignore
#-----------READ A FILE--------------------------------
# myfile = open("01 basics/010 fruits.txt")
# # print(myfile.read())
# '''
# after read(), cursor is at EOF
# '''
# # print(myfile.read())

# #----------store contents of file------------------------
# content = myfile.read()
# print(content)
# print(content)

# #---------close file-------------------------------------
# myfile.close()
# contents2 = myfile.read()   #error

#------------ALTERNATIVE----------------------------------
# with open('01 basics/010 fruits.txt') as myfile:
#     content = myfile.read()
#     #with context manager closes the file implicitly
# print(content)

#----------write to a file------------
# with open('01 basics/010 vegetables.txt','w') as myfile:
#     # myfile.write('Tomato\nPotato\nOnion\nGarlic')
#     # or
#     myfile.write('Tomato\n')
#     myfile.write('Potato\n')
#     myfile.write('Onion\n')
#     myfile.write('Garlic\n')
#     myfile.write('Cucumber')
#     '''
#         'r' mode:  reads a file
#         'w' mode:  overwrites an existing file, creates a new file if not present
#     '''

#----------append to a file------------
# with open('01 basics/010 vegetables.txt','a') as myfile:
#     '''
#         'a' mode: append file, concatenate text at end
#     '''
#     myfile.write('\nCarrot')
#     # print(myfile.read())    #error, file operation not supported

#----------append and read to a file------------
with open('01 basics/010 vegetables.txt','a+') as myfile:
    '''
        'a+' mode: append + read file, concatenate text at end and read file
    '''
    myfile.write('\nCabbage')
    myfile.seek(0)  #moves the read/write cursor to start of file
    print(myfile.read())
