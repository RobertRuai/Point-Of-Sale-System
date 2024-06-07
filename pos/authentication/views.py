from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib import messages


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            messages.succes(request, 'User created - please <a href="/login">login</a>.')

            return redirect("/login/")

        else:
            messages.error(request, 'Form is not valid')
    else:
        form = SignUpForm()

    return render(request, "authentication/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)


    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, 'Invalid username or password!')
        else:
            messages.error(request, 'An error occurred!.')

    return render(request, "authentication/login.html", {"form": form})
