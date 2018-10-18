from django.conf.urls import url
from job_seeker import views

app_name = "job_seeker"

urlpatterns = [
    url(r'^userdashboard/', views.UserDashBoard, name = "user_dashboard"),
    url(r'^profile_form/$', views.UserProfileForm, name = "user_profile_form")
]
