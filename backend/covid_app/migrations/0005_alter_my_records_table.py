# Generated by Django 4.1.4 on 2022-12-24 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0004_alter_my_records_date'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='my_records',
            table='Myrecords',
        ),
    ]