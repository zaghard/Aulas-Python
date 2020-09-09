# Manipulando data e Hora

from datetime import date, time, datetime, timedelta
#<-------------------------------------------------------------------->
def trabalhando_com_date():
    data_atual = date.today()
    # print(data_atual)
    # print(data_atual.strftime('%d/%m/%y'))
    # print(data_atual.strftime('%d/%m/%Y'))
    # print(data_atual.strftime('%A %B %Y'))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual_str))
#<-------------------------------------------------------------------->

def trabalhando_com_hora():
    horario = time(hour=15, minute=18, second=59)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario))
    print(horario)
    print(horario.strftime('%H:%M:%S'))
    print(type(horario_str))
#<-------------------------------------------------------------------->

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo' )
    print(tupla[data_atual.weekday()])
    data_criada= datetime(2021, 9, 8, 22, 10, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2020'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    # nova_data = data_convertida - timedelta(day=365)
    # print(nova_data)



if __name__ == '__main__':
    # trabalhando_com_hora()
    # trabalhando_com_date()
    trabalhando_com_datetime()

