# Generated by Django 5.0.6 on 2024-07-06 15:59

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Ad Title & Folder Name', max_length=200)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('condition', models.CharField(blank=True, choices=[('Brand New', 'Brand New'), ('Used', 'Used')], max_length=100)),
                ('color', models.CharField(choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Gold', 'Gold'), ('Green', 'Green'), ('Grey', 'Grey'), ('Navy', 'Navy'), ('Orange', 'Orange'), ('Red', 'Red'), ('Silver', 'Silver'), ('White', 'White')], max_length=100)),
                ('kilometers', models.IntegerField()),
                ('fuel', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=100)),
                ('engine_size', models.DecimalField(decimal_places=1, max_digits=2)),
                ('body_type', models.CharField(choices=[('Convertible', 'Convertible'), ('Coupe', 'Coupe'), ('Estate', 'Estate'), ('Hatchback', 'Hatchback'), ('SUV', 'SUV'), ('Saloon', 'Saloon')], max_length=100)),
                ('owners', models.IntegerField(blank=True)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual'), ('Semi-auto', 'Semi-auto'), ('CVT', 'CVT'), ('Other', 'Other')], max_length=100)),
                ('nct_due_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('date_listed', models.DateTimeField(default=datetime.datetime.now)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.carmake')),
            ],
        ),
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='images')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vehicles.carmodel')),
            ],
        ),
    ]
