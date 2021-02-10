soma = lambda a, b: a+b
subtracao = lambda a, b: a-b
contaLetras = lambda lista: [len(x) for x  in lista]

calculadora = {
    'somar': lambda a, b: a + b,
    'subtract': lambda a, b: a - b,
    'multiplica': lambda a, b: a*b,
    'divide': lambda a, b: a//b
}

print( soma(2,3) )
print( subtracao(4,3) )
listaAnimais = ['Cachorro', 'Pato', 'Urso']
print(contaLetras(listaAnimais))

sum = calculadora['somar']
prod = calculadora['multiplica']

print( sum(6,7) )
print( prod(4,5) )