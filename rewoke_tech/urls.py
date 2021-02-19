"""rewoke_tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from user import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homeview),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',views.signupview),
    path('login/',views.loginview),
    path('logout/',views.logoutview),
    path('filefield/',views.filefieldview),
    path('viewfile/',views.view_filefield),
    path('list/<pk>/',views.filefield_render_pdf_view, name='filefield_render_pdf_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
