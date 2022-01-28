# Salary

print('----prexware----')
print('36, A-block, Krishna villa \t\t \n kathlal \t\t \n 387620')

print('\n')

N=str(input('Name of employ'))

print(N)

S=int(input('Salary of Employ'))

print(S)

print('SR.No  \t Details \t Percentage(%) \t PayOff')

a = 1
b = "TA"
c = 2
d = int((S*2)/100)

print(a, '\t\t', b, '\t\t', c, '\t\t\t\t', d)

e = 2
f = "DA"
g = 5
h = int((S*5)/100)
print(e, '\t\t', f, '\t\t', g, '\t\t\t\t', h)

i = 3
j = "HRA"
k = 20
l = int((S*20)/100)
print(i, '\t\t', j, '\t\t', k, '\t\t\t', l)

m = 4
n = "PF"
o = 18
p = int((S*18)/100)
print(m, '\t\t', n, '\t\t', o, '\t\t\t', p)

print('total Salary =', (S-p+l+h+d))
