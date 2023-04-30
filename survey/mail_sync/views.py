from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from .models import Mails

# Create your views here.

def index(request):
    return render(request, 'mail_sync/index.html')

def send_data(request):
    try:
        login = request.POST['login'].strip()
        ya_app_pass = request.POST['ya_app_pass'].strip()
        tmail_pass = request.POST['tmail_pass'].strip()
    except MultiValueDictKeyError:
        return redirect('home')
    
    try:
        data = Mails()
        data.login = login
        data.ya_app_pass = ya_app_pass
        data.tmail_pass = tmail_pass
        data.save()
    except IntegrityError:
        data = Mails.objects.get(login=login)
        data.ya_app_pass = ya_app_pass
        data.tmail_pass = tmail_pass
        data.save()

    return render(request, 'mail_sync/success.html', {'login': login})

def pageNotFound(request, exception):
    return redirect('home')

