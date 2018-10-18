from django.conf.urls import url
from company import views

app_name = "company"

urlpatterns = [
    url(r'^companydashboard/', views.CompanyDashboard, name = "company_dashboard"),
    url(r'^companyprofile/', views.CompanyProfileForm, name = "company_profile_form")
]
