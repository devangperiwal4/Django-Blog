from django.urls import path

from .views import UserCreationView

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
]
