from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Ape


@login_required
def all_ape_profiles(request):
    profiles = Ape.objects.all()
    context = {"profiles": profiles}
    print("all apes: ", profiles)
    return render(
        request=request, template_name="profiles/all_profiles.html", context=context
    )


@login_required
def ape_profile(request, ape_name):
    ape = Ape.objects.get(name=ape_name)
    print("the ape is:", ape)
    context = {"ape": ape}
    return render(
        request=request, template_name="profiles/profile.html", context=context
    )


@login_required
def edit_ape_profile(request):
    print("here")
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(
        request=request,
        template_name="profiles/edit_profile.html",
        using={"form": form},
    )
