"""style_ku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from style_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', views.Main_template, name='main'),
    url(r'^katalog/', views.Katalog_template, name='katalog'),
    url(r'^1/', views.k1_template, name='1'),
    url(r'^2/', views.k2_template, name='2'),
    url(r'^3/', views.k3_template, name='3'),
    url(r'^4/', views.k4_template, name='4'),
    url(r'^5/', views.k5_template, name='5'),
    url(r'^6/', views.k6_template, name='6'),
    url(r'^about_us/', views.About_us_template, name='about_us'),
    url(r'^price/', views.Price_template, name='price'),
    url(r'^contacts/', views.Contacts_template, name='contacts'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
