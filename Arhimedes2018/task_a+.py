fifa_n = int(input())
fifa_every = int(input())
foofa_n = int(input())
foofa_every = int(input())
days = int(input())

fifa = fifa_n+fifa_every*days
foofa = foofa_n+foofa_every*days

if fifa > foofa: print('Feefa')
elif fifa == foofa: print('Draw')
else: print('Foofa')