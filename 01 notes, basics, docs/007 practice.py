def maker(phrase):
    intero = ('why','what','how','which')
    cap = phrase.capitalize()
    if phrase.startswith(intero):
        return '{}?'.format(cap)
    else: return '{}.'.format(cap)

results=[]
while True:
    inp = input('Say Something: ')
    if inp=='\end':
        break
    else:
        results.append(maker(inp))

print(' '.join(results))