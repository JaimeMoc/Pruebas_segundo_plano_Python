from django.shortcuts import render
from app1.tasks import send_mail

#Creación de nuestro index.
def index(request):
    
    mail_sent = False
    
    if  request.method == 'POST':
        email = request.POST.get('email')   
        send_mail(email)        

        mail_sent = True
    
    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
