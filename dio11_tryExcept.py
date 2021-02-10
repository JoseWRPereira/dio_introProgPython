#
# Documentação do exception
# https://docs.python.org/3/library/exceptions.html
#

lista = [1,3]
try:
    divisao = 10/1
    num = lista[1]

except ZeroDivisionError:
    print("Não é possível realizar a divisão por zero!")
#except IndexError:
    print("Erro ao acessar índice inválido!")
except BaseException as ex:
    print("Erro desconhecido. Erro: {}".format(ex))
else:
    print("Não houve erro!")
finally:
    print("SEMPRE executa o finally!!!")

