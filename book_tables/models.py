from django.conf import settings
from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)  # Table number
    seats = models.IntegerField()  # Number of seats
    available = models.BooleanField(default=True)  # Availability of the table

    def __str__(self):
        return f"Table {self.number} - Seats: {self.seats} - {'Available' if self.available else 'Not Available'}"

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Updated to use settings.AUTH_USER_MODEL
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    num_guests = models.IntegerField()

    def __str__(self):
        return f"Reservation by {self.user.username} at Table {self.table.number} on {self.reservation_time}"

