from django.shortcuts import render

#Creación de nuestro index.
def index(request):
    return render(request, 'index.html', {
        'mail_sent': False
    })

