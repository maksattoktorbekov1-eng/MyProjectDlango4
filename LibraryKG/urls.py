from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    path('books/', include('books.urls')),
    path('time/', views.current_time, name='current_time'),
]
