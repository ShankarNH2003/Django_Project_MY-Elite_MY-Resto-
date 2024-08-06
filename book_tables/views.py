from django.shortcuts import render, redirect
from .models import Table, Reservation
from .forms import ReservationForm
from django.utils import timezone

def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            # Update table availability
            if reservation.table.available:
                reservation.table.available = False
                reservation.table.save()
                reservation.save()
                return redirect('reservation_confirmation')
            else:
                form.add_error(None, 'Selected table is not available.')
    else:
        form = ReservationForm()
    return render(request, 'book_tables/reserve_table.html', {'form': form})

def view_available_tables(request):
    current_time = timezone.now()
    reservations = Reservation.objects.filter(reservation_time__gte=current_time)
    reserved_table_ids = reservations.values_list('table_id', flat=True)
    available_tables = Table.objects.filter(available=True).exclude(id__in=reserved_table_ids)
    return render(request, 'book_tables/view_available_tables.html', {'tables': available_tables})

def reservation_confirmation(request):
    return render(request, 'book_tables/reservation_confirmation.html')
