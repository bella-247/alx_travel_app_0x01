from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Listing
		fields = ['id', 'title', 'description', 'price', 'location']

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['id', 'listing', 'guest_name', 'start_date', 'end_date']

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = ['id', 'listing', 'reviewer_name', 'rating', 'comment']
