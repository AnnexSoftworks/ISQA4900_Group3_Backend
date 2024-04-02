from django.contrib import admin
from .models import Guest, Reservation, Room, Service


class GuestList(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone')
    list_filter = ('first_name', 'last_name', 'city', 'state', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ['last_name']


class ReservationList(admin.ModelAdmin):
    list_display = ('pk', 'guest', 'status', 'check_in_date', 'check_out_date')
    list_filter = ('guest', 'status', 'check_in_date', 'check_out_date')
    search_fields = ('guest', 'status', 'check_in_date', 'check_out_date')
    ordering = ['guest']


class ServiceList(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ['name']


class RoomList(admin.ModelAdmin):
    list_display = ('pk', 'room_number', 'rate', 'availability', 'category', 'status', 'services')
    list_filter = ('room_number', 'rate', 'availability', 'category', 'status', 'services')
    search_fields = ('room_number', 'rate', 'availability', 'category', 'status', 'services')
    ordering = ['room_number']


admin.site.register(Guest, GuestList)
admin.site.register(Reservation, ReservationList)
admin.site.register(Room, RoomList)
admin.site.register(Service, ServiceList)
