# Generated by Django 3.1.4 on 2021-01-25 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='name',
            new_name='model',
        ),
    ]