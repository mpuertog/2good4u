from django.shortcuts import render, render_to_response


def index(request):
    active_user = None
    if request.user.is_authenticated:
        active_user = request.user

    context = {
        'active_user': active_user,
    }
    return render(request, 'index.html', context)


def handler404(request, *args, **argv):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html')
    response.status_code = 500
    return response
