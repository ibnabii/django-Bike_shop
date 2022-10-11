from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.BikeListView.as_view(), name='bikeList')
]
