from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import SignupForm

# Create your views here.

def index(request):
    my_dict = {'header': 'My Second App'}
    return render(request, 'AppTwo/index.html', context=my_dict)

def help(request):
    my_dict = {'header': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=my_dict)

def user(request):

    # users_dict = {
    #     'users': User.objects.order_by('last_name')
    # }

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():

            print('VALIDATION SUCCESS!')
            print('First Name: ' + form.cleaned_data['first_name'])
            print('Last Name: ' + form.cleaned_data['last_name'])
            print('Email: ' + form.cleaned_data['email'])

            # x = User.objects.get_or_create(
            #             first_name=form.cleaned_data['first_name'],
            #             last_name=form.cleaned_data['last_name'],
            #             email=form.cleaned_data['email']
            # )[0]
            #
            # x.save()

            form.save(commit=True)
            return index(request)


        else:
            print("ERROR: FORM INVALID")

    return render(request, 'AppTwo/user.html', context = {'form':form})
