# yourapp/urls.py
from django.urls import path
from .views import DynamicModelCreateAPIView

urlpatterns = [
    path('upload/', DynamicModelCreateAPIView.as_view(), name='create_dynamic_model'),
    # Add other URL patterns as needed
]
