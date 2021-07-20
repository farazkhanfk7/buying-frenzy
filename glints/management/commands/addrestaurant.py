import json
from django.core.management.base import BaseCommand, CommandError
from glints.models import Restaurant, Menu, OpeningTime
from glints.helpers import get_schedule, weekdays

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)
        try:
            for restaurant in data_list:
                restaurant_data = restaurant.copy()
                restaurant.pop('menu')
                restaurant.pop('openingHours')
                restaurant_obj = Restaurant.objects.create(**restaurant)
                for menu in restaurant_data['menu']:
                    menu_obj = Menu.objects.create(**menu)
                    menu_obj.save()
                    restaurant_obj.menu.add(menu_obj)
                opening_hours = restaurant_data['openingHours']
                schedule = get_schedule(opening_hours)
                for day in schedule:
                    opening_time = OpeningTime(weekday=weekdays[day],from_hour=schedule[day][0],to_hour=schedule[day][1])
                    opening_time.save()
                    restaurant_obj.openingHours.add(opening_time)
                restaurant_obj.save()
            self.stdout.write(self.style.SUCCESS('Objects succesfully added to database.'))
        except Exception as e:
            raise CommandError(f"{e}")
