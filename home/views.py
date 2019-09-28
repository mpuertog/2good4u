from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.contrib.auth import login as auth_login, logout, authenticate
from django.http import HttpResponseRedirect
from home.forms import FormLogin, FormSignup
from asesorappConfig.models import Usuario


def index(request):
    active_user = None

    if request.user.is_authenticated:
        active_user = request.user
    context = {
        'active_user': active_user,
    }
    return render(request, 'index.html', context)


def login_view(request):
    form_login = FormLogin()
    if request.method == 'POST':
        form_login = FormLogin(request.POST)
        email = request.POST.get('email_login')
        raw_password = request.POST.get('password_login')
        user = authenticate(username=email, password=raw_password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, '¡El usuario o la contraseña son incorrectos!')
    return render(request, 'login.html', {'form_login': form_login})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup_view(request):
    if request.method == 'POST':
        try:
            form_registro = FormSignup(request.POST)
            if form_registro.is_valid():
                data = request.POST
                username = data.get('username')
                first_name = data.get('first_name')
                last_name = data.get('last_name')
                password = data.get('password')
                mobile = data.get('mobile')
                document = data.get('document')

                try:
                    User.objects.create_user(username=username, email=username, password=password,
                                             first_name=first_name,
                                             last_name=last_name)

                    user = User.objects.get(username=username)

                    Usuario.objects.create(user_id=user.id, numero_telefono=mobile, esAbogado=False, numero_cedula=document)
                    messages.add_message(request, messages.INFO, 'Usuario creado exitosamente, por favor inicie sesión')
                except Exception as error:
                    print(error)
                    messages.add_message(request, messages.WARNING, 'Algo ha salido mal')
                return render(request, 'index.html', )
            else:
                messages.add_message(request, messages.ERROR, form_registro.errors)
                form_registro = FormSignup()
        except Exception as error:
            print(error)
            messages.add_message(request, messages.ERROR, 'Error al crear el usuario, por favor valide los datos')
    else:
        form_registro = FormSignup()
    context = {
        'form_registro': form_registro,
    }
    return render(request, 'signup.html', context)


def handler404(request, *args, **argv):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html')
    response.status_code = 500
    return response

def new_case(request):
    return render(request, 'new_case.html')
