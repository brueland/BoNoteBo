from django import forms
from .models import Ape, HealthRecord


class ProfileForm(forms.ModelForm):
    class Meta:
        ape_model = Ape
        ape_fields = [
            "name",
            "age",
            "sex",
            "profile_picture",
        ]
        health_record_model = HealthRecord
        health_record_fields = ["weight", "stool_type", "swelling", "status"]
