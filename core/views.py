from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, redirect

from .forms import SignUpForm

def index(request):
    return render(request, 'core/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("/rooms/")
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            print(user)
            login(request, user)
            return redirect("/rooms/")

        else:
            # No backend authenticated the credentials
            return render(request, 'core/login.html',{'form':"Username or Password is incorrect"})

    return render(request, 'core/login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
