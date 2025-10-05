from rest_framework import viewsets

from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    

class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
