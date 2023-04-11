from datetime import date

from rest_framework import generics
from django.db.models import Count, Q

from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer


# 4 question
class HotelAPIView(generics.ListAPIView):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_queryset(self):

        today = date.today()
        return Hotel.get_hotel_with_only_one_free_room(today)



# 3 question
class RoomAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        move_in = self.kwargs['move_in']
        move_out = self.kwargs['move_out']
        return Room.get_rooms_list_with_sold_out_sign(move_in, move_out)