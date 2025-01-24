from django.shortcuts import render
from app1.tasks import send_mail

from datetime import datetime
from datetime import timedelta

#Creación de nuestro index.
def index(request):
    
    mail_sent = False
    
    if  request.method == 'POST':
        email = request.POST.get('email')   
        
        # send_mail.delay(email)    Tarea que consume computacionalmente más tiempo     

        send_mail.apply_async(
            args = [email],
            # countdown = 10  Nos permite decirle que se envie despeus de 10 seg.
            eta = datetime.now() + timedelta(seconds=30) #Nos permite agregar un lapso de tiempo más grande. 
        )
        
        mail_sent = True
    
    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
