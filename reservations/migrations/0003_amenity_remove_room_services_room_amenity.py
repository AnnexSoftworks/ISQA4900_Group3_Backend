# Generated by Django 4.2.10 on 2024-04-02 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_rename_availability_status_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='services',
        ),
        migrations.AddField(
            model_name='room',
            name='amenity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='reservations.amenity'),
            preserve_default=False,
        ),
    ]
