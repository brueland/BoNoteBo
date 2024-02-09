# nutrition/models.py
from django.db import models
from profiles.models import Ape


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories_per_unit = models.PositiveIntegerField()
    food_icon = models.ImageField(
        upload_to="media/nutrition_icons/", null=True, blank=True
    )

    def __str__(self):
        return self.name


class FeedingEvent(models.Model):
    apes = models.ManyToManyField(Ape, related_name="feeding_events")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ape_names = ", ".join(ape.name for ape in self.apes.all())
        return f"{self.food_item.name} fed to {ape_names} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"
