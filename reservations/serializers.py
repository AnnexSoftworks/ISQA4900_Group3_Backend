from django.contrib.auth.models import User
from .models import Guest, Reservation, Room, Service, RoomType, Status
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('pk', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone')


class ReservationSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    status_name = serializers.SerializerMethodField()
    room_number = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ('room_number', 'first_name', 'last_name', 'status_name', 'check_in_date', 'check_out_date')

    def get_first_name(self, obj):
        return obj.guest.first_name

    def get_last_name(self, obj):
        return obj.guest.last_name

    def get_status_name(self, obj):
        return obj.status.status

    def get_room_number(self, obj):
        return obj.room.room_number


class RoomSerializer(serializers.ModelSerializer):
    room_type_name = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('pk', 'room_number', 'guest_limit', 'room_type_name', 'rate', 'status')

    def get_room_type_name(self, obj):
        return obj.room_type.name

    def get_rate(self, obj):
        return obj.room_type.rate


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
