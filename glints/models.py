from django.db import models
from django.utils.translation import ugettext_lazy as _

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
