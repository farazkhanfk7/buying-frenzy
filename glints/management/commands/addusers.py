import json
import pytz
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from glints.models import Buyer, Purchase
from glints.helpers import get_schedule, weekdays

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)
        try:
            for user in data_list:
                user_data = user.copy()
                user.pop('purchaseHistory')
                buyer_obj = Buyer.objects.create(**user)
                buyer_obj.save()
                for purchase in user_data['purchaseHistory']:
                    purchase['purchaser'] = buyer_obj
                    date_time = purchase['transactionDate']
                    d = datetime.strptime(date_time, "%m/%d/%Y %I:%M %p")
                    new_date_time = d.strftime('%Y-%m-%d %H:%M')
                    purchase['transactionDate'] = new_date_time
                    purchase_obj = Purchase.objects.create(**purchase)
                    purchase_obj.save()
            self.stdout.write(self.style.SUCCESS('Objects succesfully added to database.'))
        except Exception as e:
            raise CommandError(f"{e}")
