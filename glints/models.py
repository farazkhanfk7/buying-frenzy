from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
import uuid

# Create your models here.
WEEKDAYS = [
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (7, _("Sunday")),
]

class Menu(models.Model):
    dishName = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return f"{self.dishName}"

class OpeningTime(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    def __str__(self):
        return f"{self.weekday}-{self.from_hour}-{self.to_hour}"


class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=255)
    cashBalance = models.FloatField()
    menu = models.ManyToManyField(Menu,related_name='available_in', blank=True)
    openingHours = models.ManyToManyField(OpeningTime, blank=True)

    def __str__(self):
        return f"{self.restaurantName}"

class Buyer(models.Model):
    id = models.IntegerField(primary_key=True)
    cashBalance = models.FloatField()
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.id}-{self.name}"

class Purchase(models.Model):
    purchase_id = models.CharField(max_length=30, unique=True, default=uuid.uuid4)
    purchaser = models.ForeignKey(Buyer, related_name='purchaseHistory', on_delete=CASCADE)
    menu_bought = models.ForeignKey(Menu, on_delete=DO_NOTHING, blank=True, null=True, unique=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=DO_NOTHING, blank=True, null=True, unique=False)
    dishName = models.CharField(max_length=255, blank=True)
    restaurantName = models.CharField(max_length=255, blank=True)
    transactionAmount = models.FloatField(blank=True)
    transactionDate = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.purchaser}-{self.dishName}-{self.purchase_id}"


    
