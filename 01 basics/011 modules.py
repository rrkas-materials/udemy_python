import time         #built in library
import os           #standard library, but not built in
#pip3 install pandas
import pandas       #third party package/ library

# '''
# lists all the in built modules
# import sys
# print(sys.builtin_module_names)
# '''

filename = '01 basics/011 temps_today.csv'
counter = 0
while True:
    if os.path.exists(filename):
        data = pandas.read_csv(filename)
        print(data.mean())
        print(data.mean()['st1'])
        print('--------------------------------------',counter)
        counter = counter + 1
    else:
        print('File does not exists')
    time.sleep(3)