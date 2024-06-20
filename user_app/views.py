from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# Sigup


def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Congratulations!! Your account has been created"
                )
                HttpResponseRedirect("/login/")
        else:
            form = SignUpForm()
        return render(request, "signup.html", {"form": form})
    else:
        return HttpResponseRedirect("/")


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/")
        else:
            form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        return HttpResponseRedirect("/")


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")
