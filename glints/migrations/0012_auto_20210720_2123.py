# Generated by Django 3.1.4 on 2021-07-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glints', '0011_auto_20210720_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='id',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_id',
            field=models.CharField(default='10fe2863-8af1-46db-ab49-1ee80b4436cb', max_length=30, primary_key=True, serialize=False),
        ),
    ]