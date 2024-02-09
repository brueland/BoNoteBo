from django.contrib import admin
from .models import FoodItem, FeedingEvent

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(FeedingEvent)
