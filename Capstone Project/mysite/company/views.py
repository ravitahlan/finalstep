from django.shortcuts import render

# Create your views here.

def CompanyDashboard(request):
    return render(request, "company_dashboard.html", {})

def CompanyProfileForm(request):
    return render(request, "company_profile_form.html", {})
