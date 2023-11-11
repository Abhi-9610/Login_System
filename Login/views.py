from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse 
from .utils import  send_verification_email


def home(request):
    
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':  # Should be 'POST' in uppercase
        username = request.POST.get('Username', '')
        fname = request.POST.get('Firstname', '')
        lname = request.POST.get('Lastname', '')
        email = request.POST.get('Email', '')
        pass1 = request.POST.get('Password', '')
        pass2 = request.POST.get('ConfirmPassword', '')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists!!Please try another")
            return redirect('signup')
        if User.objects.filter(email=email):
            messages.error(request,"Email already assosicated with other Account!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if len(username) < 4 or len(username) > 10:
            messages.error(request, "Length of the username must be between 4 and 10 characters.")
            return redirect('signup')
        
            # Check if the passwords match
        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        
        user.last_name = lname
        user.save()
        messages.success(request, "Account created successfully.")
       

        send_verification_email(user)


        return redirect('signin')
        
        
            

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']  # Should be 'password' instead of 'pass1'

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Successfully!!")
            return render(request, "index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')
    
    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')




