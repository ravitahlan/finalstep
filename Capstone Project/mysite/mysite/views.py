from django.views.generic import TemplateView
from django.shortcuts import render, redirect
# from django.views.generic import View
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect, HttpResponse
# from editor.forms import UserForm, LoginForm
# from django.contrib.auth.decorators import login_required
# from django import forms
# from django.contrib.auth import login, logout, authenticate

def HomePage(request):
    return render(request, "index.html", {})
