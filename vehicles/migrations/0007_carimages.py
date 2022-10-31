# Generated by Django 3.2.9 on 2022-10-31 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_auto_20210221_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='images')),
                ('ad_title', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicles.carmodel')),
            ],
        ),
    ]
