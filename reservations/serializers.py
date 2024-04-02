from django.contrib.auth.models import User
from .models import Guest, Reservation, Room, Service
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('pk', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('pk', 'guest', 'status', 'check_in_date', 'check_out_date')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('pk', 'room_number', 'rate', 'availability', 'category', 'status', 'service')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('pk', 'name', 'description')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True,
                                     style={'input_type': 'password'}, validators=[validate_password])
    password2 = serializers.CharField(write_only=True,
                                      style={'input_type': 'password'}, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email',
                  'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True, 'min_length': 6},
            'password2': {'write_only': True, 'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'is_superuser', 'first_name',
                  'last_name', 'email')
