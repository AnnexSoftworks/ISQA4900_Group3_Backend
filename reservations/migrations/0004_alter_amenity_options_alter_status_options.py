# Generated by Django 4.2.10 on 2024-04-02 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_amenity_remove_room_services_room_amenity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name': 'Amenity', 'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
    ]