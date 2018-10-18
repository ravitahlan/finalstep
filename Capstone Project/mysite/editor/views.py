from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def typingEditor(request):
    return render(request, "editor/typing_master.html",{})
