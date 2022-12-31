import keyboard, time, sys
from threading import Thread

vlr_tecla = {"value": 0}

def monitorKey():
    while True:
        if keyboard.is_pressed('space'):
            print('\033[31m'+'Tecla de espaço pressionada e o RPA parou'+'\033[m')
            vlr_tecla['value'] += 1
            break    
Thread(target = monitorKey).start()

lista = [1,2,3,4,5,6,7,8] 

while vlr_tecla['value'] == 0:
    print('\033[33m'+'>>> Olá Mundo'+'\033[m')
    for numero in lista:        
        #Condição de parada
        if(vlr_tecla['value'] != 0):
            break
        print('\033[32m'+ str(numero) +'\033[m')
        time.sleep(1)
print('\033[31m'+'Programa terminou'+'\033[m')
# https://pt.stackoverflow.com/questions/532117/como-interromper-um-script-em-andamento-com-uma-tecla 