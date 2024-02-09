# profiles/models.py
from django.db import models

SEX_CHOICES = [("M", "Male"), ("F", "Female"), ("U", "Unknown")]
TUMESCENCE_CHOICES = [
    ("1", "No swelling and flaccid skin with many wrinkles"),
    ("2", "Half tumescent"),
    ("3", "Maximal tumescence - very taught skin with no wrinkles or sags"),
    ("NA", "Not Applicable"),
]

STOOL_TYPE_CHOICES = [
    ("1", "Type 1: Separate hard lumps, like nuts (hard to pass)"),
    ("2", "Type 2: Sausage-shaped but lumpy"),
    ("3", "Type 3: Like a sausage but with cracks on the surface"),
    ("4", "Type 4: Like a sausage or snake, smooth and soft"),
    ("5", "Type 5: Soft blobs with clear-cut edges (easy to pass)"),
    ("6", "Type 6: Fluffy pieces with ragged edges, a mushy stool"),
    ("7", "Type 7: Watery, no solid pieces (entirely liquid)"),
    ("NA", "Not Applicable"),
]

STATUS_CHOICES = [
    ("BAR", "Bright, alert, responsive"),
    ("QAR", "Quiet, alert, responsive"),
    ("GA", "Good appetite"),
    ("PA", "Poor appetite"),
    ("GH", "Good hydration"),
    ("PH", "Poor hydration"),
    ("NBM", "Normal bowel movement"),
    ("SS", "Soft stool"),
    ("DIA", "Diarrhea"),
    ("NSP", "No signs of pain"),
]


class Status(models.Model):
    code = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return f"{self.code} - {self.description}"


class Ape(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="U")
    profile_picture = models.ImageField(
        upload_to="media/ape_profiles/", null=True, blank=True
    )
    swelling = models.CharField(max_length=2, choices=TUMESCENCE_CHOICES, default="NA")
    stool_type = models.CharField(
        max_length=2, choices=STOOL_TYPE_CHOICES, default="NA"
    )
    status = models.ManyToManyField(Status, related_name="apes", blank=True)

    def __str__(self):
        return self.name
