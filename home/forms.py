from django.contrib.auth import password_validation
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from django.forms import Form


class FormSignup(Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.EmailField(max_length=254, help_text='Email', required=True,
                                error_messages={'required': 'Ingrese una dirección de correo válida'})
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    mobile = forms.CharField(max_length=10, required=True)
    document = forms.CharField(max_length=20, required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Este usuario ya existe')
        return username

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        try:
            password_validation.validate_password(password2)
        except password_validation.ValidationError as errores:
            mensajes = []
            for m in errores.messages:
                if m == 'This password is too short. It must contain at least 8 characters.':
                    mensajes.append('Contraseña muy corta, debe contener más de 7 caracteres')
                if m == 'This password is too common.':
                    mensajes.append('Contraseña muy común')
                if m == 'This password is entirely numeric.':
                    mensajes.append('Contraseña no puede contener solo números')
                if m.startswith("The password is too similar"):
                    mensajes.append('Contraseña muy similar a los datos del usuario')
            raise forms.ValidationError(mensajes)
        return password2


class FormLogin(forms.Form):
    email_login = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Usuario'
    )
    password_login = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contraseña'
    )
