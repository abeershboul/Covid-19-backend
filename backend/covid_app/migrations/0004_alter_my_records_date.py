# Generated by Django 4.1.4 on 2022-12-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0003_remove_my_records_status_my_records_total_deaths_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_records',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
