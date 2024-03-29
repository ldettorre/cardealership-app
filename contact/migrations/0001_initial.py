# Generated by Django 3.1.4 on 2021-01-25 01:14

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarSourcing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\d+$')])),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=100)),
                ('variant', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('condition', models.CharField(blank=True, choices=[('Brand New', 'Brand New'), ('Used', 'Used')], max_length=100)),
                ('fuel', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=100)),
                ('additional_information', models.TextField(max_length=250)),
                ('gdpr_aggrement', models.BooleanField(default=True)),
                ('submission_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField(max_length=250)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\d+$')])),
                ('submission_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
