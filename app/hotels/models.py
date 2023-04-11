from django.db import models
from django.db.models import Case, Q, Sum, When
from users.models import User


class Hotel(models.Model):
    title = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

    # 4 question
    @classmethod
    def get_hotel_with_only_one_free_room(cls, today):
            return cls.objects.annotate(
                free_room = Sum(
                        Case(
                            When(rooms__reservations__start__lte=today, rooms__reservations__end__gte=today, then=0),
                            output_field=models.IntegerField(),
                            default=1,
                            distinct=True
                        )
                )
            ).filter(free_room=1).values("title", "free_room")


class Room(models.Model):
    title = models.CharField(max_length=128)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')

    # 3 question
    @classmethod
    def get_rooms_list_with_sold_out_sign(cls, move_in, move_out):
            return cls.objects.annotate(
                sold_out = Case(
                        When(reservations__start__lte=move_in, reservations__end__gte=move_in, then=True),
                        When(reservations__start__lte=move_out, reservations__end__gte=move_out, then=True),
                        output_field=models.IntegerField(),
                        default=False,
                        distinct=True
                    )
            ).values(
                'sold_out',
                'title'
            )



class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
