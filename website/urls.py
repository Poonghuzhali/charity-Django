from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('causes/', views.causes, name='causes'),
    path('donate/thank-you/', views.thank_you, name='thank_you'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('volunteer/', views.volunteer, name='volunteer'),
]
