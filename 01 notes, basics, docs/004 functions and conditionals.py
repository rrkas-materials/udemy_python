'''
Note:
    a function returning nothing returns None implicitly!
'''


def mean(value):
    if type(value) ==list:      #same as : if isinstance(value, list)
        val = sum(value)/len(value)
    elif type(value) == dict:
        val = sum(value.values())/len(value)
    else: val = 0.0
    return val

print(mean([1,2,3,4,5]))
print(mean({"a":1,"b":3}))