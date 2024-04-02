from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Guest(models.Model):
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    loyalty_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.loyalty_number)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')
    status = models.CharField(max_length=200)
    check_in_date = models.DateField(default=timezone.now, blank=True, null=True)
    check_out_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.guest)

    def cust_number(self):
        return self.guest.loyalty_number


class RoomType(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    rate = models.DecimalField(max_digits=10, decimal_places=2)


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)


class Room(models.Model):
    room_number = models.IntegerField(blank=False, null=False)
    guest_limit = models.IntegerField(blank=False, null=False)
    rate = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='+')
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='+')  # room type/view
    services = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='+')  # room accommodations
    status = models.CharField(max_length=12)

    def created(self):
        self.recent_date = timezone.now()
        self.save()


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    method = models.CharField(max_length=64)
    status = models.CharField(max_length=64)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    role = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
