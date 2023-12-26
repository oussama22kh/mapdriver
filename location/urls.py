from django.urls import path
from . import views

urlpatterns = [
    path('api/<int:pk>', views.location.as_view()),
]
