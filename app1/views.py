from django.shortcuts import render
from app1.tasks import asyn_send_mail

#Creación de nuestro index.
def index(request):
    
    mail_sent = False
    
    if  request.method == 'POST':
        email = request.POST.get('email')   
        asyn_send_mail(email)    #Tarea que consume computacionalmente más tiempo     

        mail_sent = True
    
    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
