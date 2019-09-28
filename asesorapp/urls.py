"""asesorapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.index, name='index'),
                  url(r'^logout/$', views.logout_view, name='logout'),
                  url(r'^login/$', views.login_view, name='login'),
                  url(r'^signup/$', views.signup_view, name='signup'),
                  url(r'^new_case/$', views.new_case, name='new_case'),
                  url(r'^bid/$', views.bid, name='bid'),
                  path('casos/', views.CasosView.as_view(), name='casos'),
                  path('casos/caso/<pk>/', views.Caso_Detail.as_view(), name='caso'),
                  path('ofertas/<idCaso>/', views.Ofertas.as_view(), name='ofertas'),
                  path('usuario/<id>/', views.Usuario_Detail.as_view(), name='usuario'),
                  path('notificaciones/<idUsuario>/', views.Notificacion_Usuario.as_view(), name='notificaciones'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
