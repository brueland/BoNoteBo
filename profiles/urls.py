from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.all_ape_profiles, name="all_ape_profiles"),
    path("<str:ape_name>/", views.ape_profile, name="ape_profile"),
    path("<str:ape_name>/edit/", views.edit_ape_profile, name="edit_ape_profile"),
]
