# Generated by Django 4.2.10 on 2024-04-02 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_alter_amenity_options_alter_status_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='amenity',
        ),
        migrations.AddField(
            model_name='room',
            name='amenity',
            field=models.ManyToManyField(related_name='rooms', to='reservations.amenity'),
        ),
    ]
