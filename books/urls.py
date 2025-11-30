from django.urls import path
from . import views

urlpatterns = [
    path('',views.writers_view, name='home'),   
    path('writers/', views.writers_view, name='writers'),
    path('quotes/', views.quotes_view, name='quotes'),
    path('time/', views.time_view, name='time'),
]
