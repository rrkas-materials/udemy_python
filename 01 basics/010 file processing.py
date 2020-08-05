# my terminal is at root folder, same level as .gitignore
#-----------READ A FILE--------------------------------
# myfile = open("01 basics/010 fruits.txt")
# print(myfile.read())
# '''
# after read(), cursor is at EOF
# '''
# print(myfile.read())

# content = myfile.read()
# print(content)
# print(content)

# myfile.close()
# print(content)      #error

#------------ALTERNATIVE----------------------------------
with open('01 basics/010 fruits.txt') as myfile:
    content = myfile.read()
    #with context manager closes the file implicitly
print(content)
