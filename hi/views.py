from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.


def login_page(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
            
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully Logged in')
            return redirect('faculty')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # password validation
        if password1 == password2:
            # Check username
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=email, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'Successfully registered')
                return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'register.html')


def faculty(request):
    return render(request, 'faculty.html')
