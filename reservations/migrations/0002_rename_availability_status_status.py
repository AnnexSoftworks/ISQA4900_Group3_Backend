# Generated by Django 4.2.10 on 2024-04-02 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='availability',
            new_name='status',
        ),
    ]
