
from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet

urlpatterns = [
    path('', views.index, name='index'),  # or your actual view endpoints
    path('', include(router.urls)),
]
