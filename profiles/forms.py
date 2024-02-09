from django import forms
from .models import Ape


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Ape
        fields = [
            "name",
            "age",
            "weight",
            "sex",
            "swelling",
            "status",
            "profile_picture",
        ]
