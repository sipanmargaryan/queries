from datetime import date

from rest_framework import generics
from django.db.models import F

from hotels.models import Reservation, Hotel
from users.serializers import UserProfileSerializer
from users.models import User


# 1 question
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):

        today = date.today()
        city = self.kwargs['city']
        reservations = Reservation.objects.filter(room__hotel__city=city, start__lte=today, end__gte=today)
        return User.objects.filter(reservations__in=reservations)


# 2 question

def like_hotel_view(request, hotel_id):
    # hotel = get_object_or_404(Hotel, id=hotel_id)
    # hotel.likes += 1
    # hotel.save()

    # right
    Hotel.objects.filter(id=hotel_id).update(likes=F('likes')+1)
    # return HttpResponse({'details': 'success'})

def dislike_holet_view(request, hotel_id):
    # hotel = get_object_or_404(Hotel, id=hotel_id)
    # hotel.dislikes += 1
    # hotel.save()

    # right
    Hotel.objects.filter(id=hotel_id).update(dislikes=F('dislikes')+1)

    # return HttpResponse({'details': 'success'})