from django.shortcuts import render, HttpResponse
from .models import Mails

# Create your views here.

def index(request):
    return render(request, 'mail_sync/index.html')

def send_data(request):
    login = request.POST['login']
    ya_app_pass = request.POST['ya_app_pass']
    tmail_pass = request.POST['tmail_pass']
    
    data = Mails()
    data.login = login
    data.ya_app_pass = ya_app_pass
    data.tmail_pass = tmail_pass
    data.save()

    return render(request, 'mail_sync/success.html', {'login': login})

