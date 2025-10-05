from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'listings', views.ListingViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]
