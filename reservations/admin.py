from django.contrib import admin
from .models import Guest, Reservation, Status, RoomType, Room, Service


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


class RoomTypeList(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'rate')
    list_filter = ('name', 'rate', 'description')
    search_fields = ('name', 'rate', 'description')
    ordering = ['name']


class StatusList (admin.ModelAdmin):
    list_display = ('pk', 'availability', 'description')
    list_filter = ('availability', 'description')
    search_fields = ('availability', 'description')
    ordering = ['availability']


class RoomList(admin.ModelAdmin):
    list_display = ('pk', 'room_number', 'room_type', 'status', 'services')
    list_filter = ('room_number', 'room_type', 'status', 'services')
    search_fields = ('room_number', 'rate', 'room_type', 'status', 'services')
    ordering = ['room_number']


admin.site.register(Guest, GuestList)
admin.site.register(Reservation, ReservationList)
admin.site.register(Status, StatusList)
admin.site.register(RoomType, RoomTypeList)
admin.site.register(Room, RoomList)
admin.site.register(Service, ServiceList)