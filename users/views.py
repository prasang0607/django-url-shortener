from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings


def signin_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if not username or not password:
            messages.error(request, 'Please provide credentials.')
            return redirect(settings.LOGIN_URL)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, 'Either user does not exist or password is wrong.')
            return redirect(settings.LOGIN_URL)
    return render(request, 'users/signin.html')


@login_required()
def signout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect(settings.LOGIN_URL)
