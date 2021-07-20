# Generated by Django 3.1.4 on 2021-07-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glints', '0004_auto_20210719_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True)),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='openingHours',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='openingHours',
            field=models.ManyToManyField(blank=True, to='glints.OpeningTime'),
        ),
    ]