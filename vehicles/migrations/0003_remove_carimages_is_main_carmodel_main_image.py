# Generated by Django 5.0.6 on 2024-07-06 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_carimages_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carimages',
            name='is_main',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='main_image',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.carimages'),
            preserve_default=False,
        ),
    ]