from django.shortcuts import render, render_to_response
from django.contrib.auth import login as auth_login, logout
from django.http import HttpResponseRedirect


def index(request):
    active_user = None

    if request.user.is_authenticated:
        active_user = request.user
    context = {
        'active_user': active_user,
    }
    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def handler404(request, *args, **argv):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html')
    response.status_code = 500
    return response
