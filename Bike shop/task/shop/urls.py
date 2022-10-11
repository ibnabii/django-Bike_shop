from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.BikeListView.as_view(), name='bikeList'),
    path('bikes/<int:bike_id>/', views.BikeDetailsView.as_view(), name='bikeDetails'),
    path('order/<int:pk>/', views.OrderConfirmationView.as_view(), name='order_confirmation')
]
