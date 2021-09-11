from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("Username " + username +" Pass" + password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user=user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.info(request, 'Password did not matched')
            return redirect('register')
        elif User.objects.filter(email = email):
            messages.info(request, 'Email Already Taken')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, password=password1,
                                            username=username)
            if user is not None:
                print("User created sucessfully")
                return redirect('login')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
