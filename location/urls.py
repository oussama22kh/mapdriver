from django.urls import path
from . import views

urlpatterns = [
    path('api/<slug:pk>', views.locationDetail.as_view()),
    path('api/', views.locationList.as_view())
]
