"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from registration import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage, name='home'),
    url(r'^userlogin/$', views.UserLogin.as_view(), name = "user_login"),
    url(r'^companylogin/$', views.CompanyLogin.as_view(), name = "company_login"),
    url(r'^userlogout/$', views.user_logout, name = "user_logout"),
    url(r'^usersignup/$', views.UserSignUp, name = "user_signup"),
    url(r'^companysignup/$', views.CompanySignUp, name = "company_signup"),
    url(r'^job_seeker/',include('job_seeker.urls'), name = "job_seeker" ),
    url(r'^company/', include('company.urls'), name = "company"),
    url(r'^editor/', include('editor.urls'), name = "editor")
]
