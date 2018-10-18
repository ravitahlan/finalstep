from django.shortcuts import render

# Create your views here.
def UserProfileForm(request):
        return render(request, "user_profile_form.html", {})

def UserDashBoard(request):
    return render(request, "user_dashboard.html", context = {})
