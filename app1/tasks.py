import time
from celery import shared_task
# from threading import Thread

"""
def asyn_send_mail(to):
    task= Thread(target=send_mail, args=(to,)) #Creación de un segundo Hilo.
    task.start() 
"""
@shared_task #Decorador de la función que nos ayudara a mandarla a segundo plano.
def send_mail(to):
    time.sleep(2)
    print(">>> Hemos enviado el correo.")