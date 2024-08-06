from django.urls import path
from . import views



urlpatterns = [
    path('view-available-rooms/', views.view_available_rooms, name='view_available_rooms'),
    path('book-room/', views.book_room, name='book_room'),
    path('room-types/', views.room_types_view, name='room_types_view'),
    path('rooms/<int:room_type_id>/', views.rooms_by_type, name='rooms_by_type'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('book-room/', views.book_room, name='book_room'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
    
]
