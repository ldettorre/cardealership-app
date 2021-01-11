# Generated by Django 3.1.4 on 2021-01-06 14:58

import datetime
from django.db import migrations, models
import vehicles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Ad Title & Folder Name', max_length=200)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('condition', models.CharField(blank=True, choices=[('Brand New', 'Brand New'), ('Used', 'Used')], max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('mileage', models.IntegerField()),
                ('fuel', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=100)),
                ('engine_size', models.DecimalField(decimal_places=1, max_digits=2)),
                ('body_type', models.CharField(max_length=100)),
                ('owners', models.IntegerField(blank=True)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=100)),
                ('nct_due_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_1', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_2', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_3', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_4', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_5', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_6', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_7', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_8', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_9', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('photo_10', models.ImageField(blank=True, upload_to=vehicles.models.Vehicles.upload_photo_to)),
                ('published', models.BooleanField(default=True)),
                ('date_listed', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]