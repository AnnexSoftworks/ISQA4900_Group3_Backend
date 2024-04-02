"""
URL configuration for project - reservations app.
"""
from django.urls import path
from reservations import views

urlpatterns = [
    path('', views.guestList),
    path('api/guests/', views.guestList),
    path('api/my_guest_list/', views.myGuestList),
    path('api/guests/<int:pk>', views.getGuest),
    path('api/reservations/', views.reservationList),
    path('api/reservations/<int:pk>', views.getReservation),
    path('api/rooms/', views.roomList),
    path('api/rooms/<int:pk>', views.getRoom),
    path('api/services/', views.servicesList),
]
