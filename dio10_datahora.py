from datetime import date, time, datetime, timedelta

def data():
    dataAtual = date.today()
    print(dataAtual.strftime('%d/%m/%y'))
    print(dataAtual.strftime('%A %B %Y'))

def hora():
    horario = time(hour=10, minute=12, second=21)
    print(horario.strftime('%H:%M:%S'))

def datahora():
    dh = datetime.now()
    print(dh.strftime('%d/%m/%y %H:%M:%S'))
    diaSemana = ('Segunda', 'Terça', 'Quarta','Quinta','Sexta','Sábado','Domingo')
    print(diaSemana[dh.weekday()])

def datahorastr():
    str = '07/02/2021 10:17:21'
    dhconvertida = datetime.strptime(str,'%d/%m/%Y %H:%M:%S')
    print(type(dhconvertida))
    print(dhconvertida)
    dhdelta = dhconvertida + timedelta(days=365, hours=-5)
    print(dhdelta)

if __name__ == '__main__':
    #data()
    #hora()
    #datahora()
    datahorastr()
