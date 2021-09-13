#from django.contrib import admin
from django.urls import path
from .views import (
    BookingCreateView,
    BookingDetailView,
    BookingListView,
)

app_name = 'booking'

urlpatterns = [
    path('reserve/', BookingCreateView.as_view(), name='booking_form'),
    path('reservation/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('reservations/', BookingListView.as_view(), name='booking_list'),
]