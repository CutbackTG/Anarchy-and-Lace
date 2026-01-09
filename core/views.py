from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from core.models import Profile

def home(request):
    return render(request, "core/home.html")

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(
        request,
        "core/profile.html",
        {"profile": profile},
    )

