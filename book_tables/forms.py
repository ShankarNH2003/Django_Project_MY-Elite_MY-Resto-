from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'reservation_time', 'num_guests']
        widgets = {
            'reservation_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
