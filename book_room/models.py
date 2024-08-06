from django.db import models
from django.conf import settings
from django.utils import timezone

class RoomType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.number} - {self.room_type.name}"
    
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking by {self.user} for {self.room} from {self.start_time} to {self.end_time}"
