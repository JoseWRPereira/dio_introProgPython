import requests

def buscaRua(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    if response.status_code == 200:
        #print(response.text)
        dados = response.json()
        print(dados['logradouro'] + ', ' + dados['bairro'] + ' - ' + dados['localidade'] + '/' + dados['uf'])
    else:
        print("CEP Inválido")


if __name__=='__main__':
    buscaRua('08062010')
    buscaRua('06440260')