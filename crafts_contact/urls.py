from django.urls import path
from .views import ContactAPIView, contact_us_view

urlpatterns = [
    path('contact-us/', contact_us_view, name='contact_us'),  # For rendering HTML
    path('api/contact-us/', ContactAPIView.as_view(), name='contact_us_api'),  # For handling API requests
]
