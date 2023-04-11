from django.urls import path

from .views import HotelAPIView, RoomAPIView

urlpatterns = [
    path('free-rooms', HotelAPIView.as_view()),
    path('sold-out/<str:move_in>/<str:move_out>/', RoomAPIView.as_view()),
]