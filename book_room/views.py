from django.shortcuts import get_object_or_404, render, redirect
from .models import Room, Booking, RoomType
from .forms import BookingForm
from django.utils import timezone

def view_available_rooms(request):
    current_time = timezone.now()
    bookings = Booking.objects.filter(start_time__gte=current_time)
    booked_room_ids = bookings.values_list('room_id', flat=True)
    available_rooms = Room.objects.filter(available=True).exclude(id__in=booked_room_ids)
    return render(request, 'book_room/view_available_rooms.html', {'rooms': available_rooms})

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user field
            booking.save()
            # Process the form data (e.g., create booking, save to the database)
            
            
            # Redirect to confirmation page
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    
    return render(request, 'book_room/book_room.html', {'form': form})


def booking_confirmation(request):
    return render(request, 'book_room/booking_confirmation.html')

def room_types_view(request):
    room_types = RoomType.objects.all()
    return render(request, 'book_room/room_types.html', {'room_types': room_types})

def rooms_by_type(request, room_type_id):
    room_type = get_object_or_404(RoomType, id=room_type_id)
    rooms = room_type.rooms.all()
    return render(request, 'book_room/rooms_by_type.html', {'room_type': room_type, 'rooms': rooms})