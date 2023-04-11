from django.urls import path

from .views import UserAPIView

urlpatterns = [
    path('<str:city>/', UserAPIView.as_view()),
]