from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register Completed")
            return redirect("login")
        else:
            messages.error(request, f"{form.errors}")
            return redirect("register")

    form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, "auth/form.html", context)


def login_view(request):
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome Back!")
                return redirect("home")
            messages.error(request, "Password or Username is incorrect")
            return redirect("login")
        messages.error(request, "Password or Username is incorrect")
        return redirect("login")
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "auth/form.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, "Bye!")
    return redirect("home")
