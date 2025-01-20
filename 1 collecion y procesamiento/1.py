lista = [
    "hola",
    12,
    34.56,
    37.E4,
    True,
    [1,2,3]
]

# longitud
len(lista)

# slice [index:count]

lista[1:2]
lista[:2]
lista[2:]

# agrega al final
lista.append(False)

#  agrega en posicion
lista.insert(1, ["a", "b", "c"])

max([1,2,3,4,5])
min([1,2,3,4,5])

del lista[4]

#copia

lista[:]
lista.copy()
list(lista)