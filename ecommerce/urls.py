from django.urls import path
from django.conf import settings
from ecommerce import views

urlpatterns = [
    path('about/', views.about, name='about'),
    # path('about/', views.about, name='about'),
]