# Generated by Django 3.1.4 on 2021-02-21 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_carmodel_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='mileage',
            new_name='kilometers',
        ),
    ]
