from django.shortcuts import render,redirect

# Create your views here.

def login_page(request):
    return render (request, 'login.html')

def register_page(request):
    if request.method == "POST":
        return redirect(request,'register.html')
        


    else:
        return render (request, 'register.html')

def faculty(request):
    return render (request, 'faculty.html')


