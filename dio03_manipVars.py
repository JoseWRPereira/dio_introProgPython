print("Operadores aritméticos e tipos de dados");
a = int( input("a = ") )
b = int( input("b = ") )


soma = a + b
subtracao = a - b
produto = a * b
divisao = a / b
divisaoInt = a // b
resto = a % b

print("Soma: {sum} {tipoSum}".format(sum=soma, tipoSum=type(soma)) )
print("Subtração: {sub} {tipoSub}".format(sub=subtracao, tipoSub=type(subtracao)))
print("Produto: {prod} {tipoProd}".format(prod=produto, tipoProd=type(produto)))
print("Divisão: {div} {tipoDiv}".format(div=divisao, tipoDiv=type(divisao)))
print("Divisão Inteira: {dvi} {tipoDvi}".format(dvi=divisaoInt, tipoDvi = type(divisaoInt)))
print("Resto: {res} {tipoResto}".format(res=resto, tipoResto=type(resto)))
