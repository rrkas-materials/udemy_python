import json
from difflib import get_close_matches

filepath = '02 app1 - dictionary app/data.json'     #terminal in root dir
data = json.load(open(filepath))


def definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        best_matches = get_close_matches(w,data.keys(),cutoff=0.8)
        if len(best_matches) == 0:
            return 'No such word!'
        else:
            inp = input('Did you mean {}? Type Y for yes and N for no: '.format(best_matches[0]))
            if(inp.lower()=='y'):
                return data[best_matches[0]]
        



word = input('Enter word: ')
defs = definition(word)
counter = 1
if type(defs) == list:
    for d in defs:
        print(counter,d)
        counter = counter + 1
elif type(defs) == str:
    print(defs)
