from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def user_login(request):
    next_page = request.GET.get('next', '/contact/')
    context = {'next': next_page}
    return render(request, 'userauth/dologin.html', context)


def dologin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    next_page = request.POST.get('next', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(next_page)
    else:
        context = {'next': next_page, 'error': 'incorrect'}
        return render(request, 'userauth/dologin.html', context)


def user_logout(request):
	logout(request)
	context = {'next': '/checkin/'}
	return render(request, 'userauth/dologin.html', context)
