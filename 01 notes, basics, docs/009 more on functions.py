# def area(l,b):
#     return 2*l+b

# def area2(l,b=5):       #b is a default arg
#     return 2*l+b

# '''
# def area2(l=5,b):
#     return 2*l+b

# default parameter before a non-default parameter leads to error

# '''


# print(area(4,5))        #13        #positional args
# print(area(b=3,l=2))    #7         #keyword args

# print(area2(5))
# print(area2(5,2))


#----------------ARBITARY NUMBER OF NON KEYWORD ARGUMENTS------------------------------

# def mean(*args):
#     return args
# print(mean(1,2,'a',2.3))    #(1, 2, 'a', 2.3)

# def mean(*args):
#     return sum(args)/len(args)
# print(mean(1,2,3,4))        #2.5

#----------------ARBITARY NUMBER OF NON KEYWORD ARGUMENTS------------------------------

# def mean(**kwargs):
#     return kwargs
# print(mean(a=1,b=2,c=3,d=4))        #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
