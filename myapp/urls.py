from django.urls import path
from .views import Registeration

urlpatterns = [
    path('', Registeration.as_view(), name = "Registration"),
]