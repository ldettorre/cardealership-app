# Generated by Django 3.1.4 on 2021-02-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20210223_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsourcing',
            name='gdpr_aggrement',
            field=models.BooleanField(default=False),
        ),
    ]