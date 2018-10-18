from django.shortcuts import render
from django.views.generic import View, CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from registration.forms import UserForm
from registration.models import UserModel
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def HomePage(request):
    return render(request, "index.html", {})

def UserDashBoard(request):
    return render(request, "user_index.html", {})

def CompanyDashBoard(request):
    return render(request, "company_index.html", {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(HomePage))

def cancel_registration(request):
    return HttpResponseRedirect(reverse(HomePage))

class UserLogin(View):
    template_name = "user_login.html"

    def get(self, request):
        return render(request, self.template_name, context = {})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if(user):
            if(user.is_active):
                login(request, user)
                # return HttpResponseRedirect(reverse(UserDashBoard))
                return HttpResponseRedirect(reverse(HomePage))
            else:
                return HttpResponse("User not active")
        else:
            return render(request, "user_login.html", context = {"message":"invalid details!"})


class CompanyLogin(View):
    template_name = "company_login.html"
    def get(self, request):
        return render(request, self.template_name, context = {})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if(user):
            if(user.is_active):
                login(request, user)
                # return HttpResponseRedirect(reverse(CompanyDashBoard))
                return HttpResponseRedirect(reverse(HomePage))
            else:
                return HttpResponse("User not active")
        else:
            return render(request, "company_login.html", context = {"message":"invalid details!"})

def UserSignUp(request):
    if(request.method == "POST"):
        form1 = UserForm(request.POST)
        if(form1.is_valid()):
            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            retype_password = form1.cleaned_data['confirm_password']
            User.objects.create_user(username = username, email = email, password = password, first_name = "job_seeker")
            messages.success(request, 'user registration successful')
            usr = authenticate(username = username, password = password)
            login(request, usr)
            user_instance  = UserModel(user = usr, accountType = "job_seeker")
            user_instance.save()
            # return HttpResponseRedirect(reverse(UserDashBoard))
            return HttpResponseRedirect(reverse(HomePage))
    else:
        form1 = UserForm()
    return render(request, 'user_signup.html', {'reg_form':form1})


def CompanySignUp(request):
    if(request.method == "POST"):
        form1 = UserForm(request.POST)
        if(form1.is_valid()):
            username = form1.cleaned_data['username']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            retype_password = form1.cleaned_data['confirm_password']
            User.objects.create_user(username = username, email = email, password = password, first_name = "company")
            messages.success(request, 'user registration successful')
            usr = authenticate(username = username, password = password)
            login(request, usr)
            user_instance  = UserModel(user = usr, accountType = "company")
            user_instance.save()
            # return HttpResponseRedirect(reverse(CompanyDashBoard))
            return HttpResponseRedirect(reverse(HomePage))
            # return render(request, "company_index.html", {})
    else:
        form1 = UserForm()
    return render(request, 'company_signup.html', {'reg_form':form1})
