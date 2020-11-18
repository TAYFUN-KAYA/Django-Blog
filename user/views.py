from django.shortcuts import render,HttpResponse,redirect

from .forms import RegisterForms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from .forms import LoginForm
# Create your views here.

def register(request):

    form=RegisterForms(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla kayıt oldunuz...")
        return redirect("index")

    context={
        "form":form
    }
    return render(request,"register.html",context)






    """
    if request.method=="POST":
        form=RegisterForms(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            newUser=User(username=username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            return redirect("index")
        context={
            "form":form
        }
        return render(request,"register.html",context)
    else:
        form=RegisterForms()
        context={
            "form":form
        }
        return render(request,"register.html",context)
    
    """

def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Şifre veya kullanıcı adı hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"çıkışyapıldı")
    return redirect("index")