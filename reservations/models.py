from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Guest(models.Model):
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    loyalty_number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.loyalty_number}'


class Status(models.Model):
    status = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.status


class RoomType(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=512)

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.IntegerField()
    guest_limit = models.IntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE, related_name='rooms')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f'Room {self.room_number} - Type: {self.room_type}'


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='reservations')
    check_in_date = models.DateField(default=timezone.now, blank=True, null=True)
    check_out_date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'Reservation for {self.guest} - Status: {self.status}'


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    method = models.CharField(max_length=64)
    status = models.CharField(max_length=64)

    def __str__(self):
        return f'Payment of {self.amount} - Status: {self.status}'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    role = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.role}'
