# Generated by Django 5.0.2 on 2024-04-10 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0006_devices_delivery_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('review_description', models.TextField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='device_review', to='devices.devices')),
            ],
        ),
    ]
