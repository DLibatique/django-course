from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.

def index(request):
    my_dict = {'header': 'My Second App'}
    return render(request, 'AppTwo/index.html', context=my_dict)

def help(request):
    my_dict = {'header': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=my_dict)

def user(request):

    users_dict = {
        'users': User.objects.order_by('last_name')
    }

    return render(request, 'AppTwo/user.html', context = users_dict)
