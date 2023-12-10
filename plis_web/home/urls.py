from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # Add more URLs for other pages if needed
]
