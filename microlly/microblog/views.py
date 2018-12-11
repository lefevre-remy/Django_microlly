from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from microblog.forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def newpost(request):
    return render(request, 'newpost.html')

def editpost(request):
    return render(request, 'editpost.html')

def lastposts(request):
    return render(request, 'lastposts.html')