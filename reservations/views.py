from rest_framework import status, generics
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from django.http import JsonResponse
from .models import Reservation, Guest, Room, Status, RoomType
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
import json


@api_view(['GET', 'POST'])
def guestList(request):
    # Retrieve or update the guest list.
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def guestList(request):
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        # if employee not specified, set the guest id of the person requesting
        # the new guest as the employee/agent for this customer
        if 'employee' not in request.data.keys():
            request.data['employee'] = request.user.id

        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getGuest(request, pk):
    # Retrieve, update or delete a guest instance.
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestSerializer(guest, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reservationList(request):
    # Retrieve or update the reservation list.
    if request.method == 'GET':
        reservation = Reservation.objects.all()
        serializer = ReservationSerializer(reservation, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getReservation(request, pk):
    # Retrieve, update or delete a reservation instance.
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def roomList(request):
    # Retrieve or update the room list.
    if request.method == 'GET':
        room = Room.objects.all()
        serializer = RoomSerializer(room, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getRoom(request, pk):
    # Retrieve, update or delete a stock instance.
    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(room, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterView(generics.CreateAPIView):
    # Register a new user - requester need not be authorized
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET', 'POST'])
def myGuestList(request):
    if request.method == 'GET':
        guests = Guest.objects.filter(agent=request.user)
        serializer = GuestSerializer(guests, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUser(request):
    # Request the information about the user making the request
    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def servicesList(request):
    if request.method == 'GET':
        service = Service.objects.all()
        serializer = ServiceSerializer(service, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        guest_id = request.user.id  # Assuming the user is logged in and this is a protected view
        check_in_date = parse_date(data.get('check_in_date'))
        check_out_date = parse_date(data.get('check_out_date'))
        total_guests = data.get('totalGuests')

        # You need to add logic to find an available room and create a reservation
        # Example logic (you should improve it based on your actual requirements):
        available_room = Room.objects.filter(status__status='available').first()
        if not available_room:
            return JsonResponse({'error': 'No rooms available'}, status=400)

        guest = Guest.objects.get(pk=guest_id)
        status = Status.objects.get(status='booked')
        room_type = available_room.room_type

        reservation = Reservation.objects.create(
            guest=guest,
            status=status,
            room=available_room,
            room_type=room_type,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )

        return JsonResponse({'message': 'Reservation created successfully', 'reservation_id': reservation.id},
                            status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def check_availability(request):
    if request.method == "POST":
        data = json.loads(request.body)
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')

        # Filter rooms by status "Room Available"
        available_status = Status.objects.get(status='Room Available')
        available_rooms = Room.objects.filter(status=available_status)

        rooms_data = RoomSerializer(available_rooms, many=True).data

        return JsonResponse(
            {"available_rooms": rooms_data, "check_in_date": check_in_date, "check_out_date": check_out_date},
            status=200
        )

    return JsonResponse({'error': 'Invalid request method'}, status=405)
