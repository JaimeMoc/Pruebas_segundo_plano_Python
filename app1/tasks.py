import time
from threading import Thread

def asyn_send_mail(to):
    task= Thread(target=send_mail, args=(to,))
    task.start()

def send_mail(to):
    time.sleep(2)
    print(">>> Hemos enviado el correo.")