from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Branch
from .forms import PersonForm
from django.http import JsonResponse
import json


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, "newpage.html")
        else:
            return redirect('login')
    return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username not match')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
    return render(request, "register.html")

def Customer_forms(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Application Accepted')
            return render(request, "logout.html")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            messages.error(request, 'Please fill all forms correctly.')  
            return render(request, "form.html")  
    else:  
        form = PersonForm()
    return render(request, "form.html", {"form": form})


def branches(request):
    data = json.loads(request.body)
    branches = Branch.objects.filter(district__id=data['user_id'])
    print(branches)
    return JsonResponse(list(branches.values("id", "name")), safe=False)

def logout(request):
    auth.logout(request)
    return redirect('/')