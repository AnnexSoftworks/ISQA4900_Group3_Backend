"""
URL configuration for project - reservations app.
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from reservations import views

urlpatterns = [
    path('', views.guestList),
    path('api/guests/', views.guestList),
    path('api/my_guest_list/', views.myGuestList),
    path('api/guests/<int:pk>', views.getGuest),
    path('api/reservations/', views.reservationList, name='reservation_list'),
    path('api/reservations/<int:pk>', views.getReservation),
    path('api/rooms/', views.roomList),
    path('api/rooms/<int:pk>', views.getRoom),
    path('api/services/', views.servicesList),
    path('api/create_reservation/', views.create_reservation, name='create_reservation'),
    path('api/check_availability/', views.check_availability, name='check_availability'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
