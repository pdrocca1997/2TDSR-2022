lista=[50,90,3,1.2345,True,False,'Oi']
print(lista)

print(lista[2])

lista.append(1)
lista.append('Pedro')

print(lista)

lista.insert(1,199)

print(lista)

del lista[4]
print(lista)

listinha=['a','b']
lista.insert(1,listinha)
print(lista)
del lista[2]
print(lista)
print(lista[1:4])
print(lista[ : :2])
print(lista[ 1:5:1])

lista += listinha
print(lista)

total= sum(lista)
print(total)


