# Generated by Django 3.1.4 on 2021-07-20 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glints', '0005_auto_20210719_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openingtime',
            name='weekday',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')]),
        ),
    ]