from django.shortcuts import render
from core.app1.tasks import send_mail

#Creación de nuestro index.
def index(request):
    
    mail_sent = False
    
    if  request.method == 'POST':
        email = request.POST.get('email')   
        
        # send_mail.delay(email)    Tarea que consume computacionalmente más tiempo     

        send_mail.apply_async(
            args = [email],
            countdown = 10    
        )
        
        mail_sent = True
    
    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
