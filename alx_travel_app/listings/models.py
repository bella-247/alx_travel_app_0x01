from django.db import models


# Create your models here.
class Listing(models.Model):
    """
    Represents a property available for booking.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    """
    Represents a customer's booking of a listing.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"Booking by {self.guest_name} for {self.listing.title}"
    
    
class Review(models.Model):
    """
    Represents a review for a listing.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.listing.title}"