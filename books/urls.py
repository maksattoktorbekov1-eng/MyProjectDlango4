from django.urls import path
from .views import writer_list, writer_detail

urlpatterns = [
    path('', writer_list, name='writer_list'),
    path('<int:pk>/', writer_detail, name='writer_detail'),
]
