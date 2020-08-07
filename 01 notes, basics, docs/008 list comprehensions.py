#--------SIMPLE LIST COMPREHENSION------------------------------------------------
# temps = [221, 234, 340, 230]
# new_temps= [temp / 10 for temp in temps]
# print(new_temps)        #[22.1, 23.4, 34.0, 23.0]

#--------CONDITIONAL LOOP COMPREHENSION-------------------------------------------
# temps = [221, 234, 340, 230, -9999]
# new_temp =[temp/10 for temp in temps if temp!=-9999]
# print(new_temp)

temps = [221, 234, 340, 230, -9999]

'''
new_temp =[temp/10 for temp in temps if temp!=-9999 else 0.0]
result:

File "/home/rohnak/PythonProjects/01 basics/008 list comprehensions.py", line 8
    new_temp =[temp/10 for temp in temps if temp!=-9999 else 0.0]
                                                           ^
Solution: reformat the line as:
'''
new_temp =[temp/10 if temp!=-9999 else 0.0 for temp in temps]
print(new_temp)