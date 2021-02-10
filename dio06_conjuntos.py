conjA = {1, 2, 5, 8, 8, 8, 3}
# não permite duplicidade
print(conjA)
conjA.add(13)
print(conjA)
conjA.remove(8)
print("\nA:")
print(conjA)
conjB = {3,4,5,6}
print("\nB:")
print(conjB)
conjuntoUniao = conjA.union(conjB)
print("\nA União B")
print(conjuntoUniao)
conjuntoInterseccao = conjA.intersection(conjB)
print("\nA Intersecção B")
print(conjuntoInterseccao)
conjuntoDiferenca1 = conjA.difference(conjB)
conjuntoDiferenca2 = conjB.difference(conjA)
print("\nA Diferença B")
print(conjuntoDiferenca1)
print("\nB Diferença A")
print(conjuntoDiferenca2)

conjuntoDifSimetrica = conjA.symmetric_difference(conjB)
print("\nA diferença Simétrica B")
print(conjuntoDifSimetrica)

print("\nPertinência")
conjC = {4,5}
print(conjB)
print(conjC)
print("\n C SubSet B")
print(conjC.issubset(conjB))
print("\n B SuperSet C")
print(conjB.issuperset(conjC))



print("Conversão de lista em conjunto")
print("remoção de duplicidade")
lista = ['cachorro', 'gato', 'gato', 'cavalo', 'cachorro']
print(lista)
conjuntoAnimais = set(lista)
print(conjuntoAnimais)
lista = list(conjuntoAnimais)
print(lista)
