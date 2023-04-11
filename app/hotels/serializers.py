from rest_framework import serializers

from .models import Hotel, Room


class HotelSerializer(serializers.ModelSerializer):
    free_room = serializers.IntegerField()
    class Meta:
        model = Hotel
        fields = ('title', 'free_room', )


class RoomSerializer(serializers.ModelSerializer):
    sold_out = serializers.BooleanField()
    
    class Meta:
        model = Room
        fields = ('title', 'sold_out', )