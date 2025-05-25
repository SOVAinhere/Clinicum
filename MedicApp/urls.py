from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from MedicApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('doctors/', views.Doctors.as_view(), name='doctors'),
    path('appointments/', views.book_appointment, name='book_appointment'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:  # Включает обработку медиафайлов в режиме отладки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
