import pywhatkit
import keyboard
import time
from datetime import datetime
telefones = ['+5551995007262']


mensagem = str(input('QUAL MENSAGEM DESEJA ENVIAR:'))
while len(telefones) >=1:
    #ENVIAR MENSAGEM PARA O TELEFONE / A  MENSAGEM / TEMPORIZADOR OBS MINIMO
    pywhatkit.sendwhatmsg(telefones[0], mensagem,datetime.now().hour,datetime.now().minute + 2)
    del telefones[0] #del e reenvia
    time.sleep(20)
    keyboard.press_and_release('ctrl + w')

