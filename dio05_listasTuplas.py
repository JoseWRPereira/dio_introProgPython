print("Listas : Mutáveis")
lista = [1, 5, 7, 3]
listaAnimais = ['cachorro', 'gato', 'galinha']
print(lista)
print(listaAnimais)

print("Elementos")
for x in lista:
    print(x)

for x in listaAnimais:
    print(x)

print("\nMínimos")
print(min(lista))
print(min(listaAnimais))

print("\nMáximos")
print(max(lista))
print(max(listaAnimais))


print("\nLista dobrada")
print(lista*2)
print(listaAnimais*2)

print("\nBusca de elemento na lista")
if 3 in lista:
    print("Elemento encontrado!")
else:
    print("Elemento NÃO encontrado!")

if 'Gato' in listaAnimais:
    print("Elemento encontrado!")
else:
    print("Elemento NÃO encontrado!")


print("\nInlcusão de elementos")
print(lista)
lista.append(9)
print(lista)

print(listaAnimais)
listaAnimais.append('lobo')
print(listaAnimais)

print("\nOrdenação de lista")
print(lista)
lista.sort()
print(lista)

print(listaAnimais)
listaAnimais.sort()
print(listaAnimais)


print("\n\nTuplas : Imutáves")
tupla = (1, 4, 18, 5)
print(tupla)
print(len(tupla))

print("\nConversão de Lista em Tupla")
print(listaAnimais)
tuplaAnimais = tuple(listaAnimais)
print(tuplaAnimais)

print("\nConversão de Tupla em Lista")
print(tupla)
listaTupla = list(tupla)
print(listaTupla)