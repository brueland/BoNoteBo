from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the profiles index.")


@login_required
def profile_view(request):
    return render(request, "profiles/profile.html")


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, "profiles/edit_profile.html", {"form": form})
