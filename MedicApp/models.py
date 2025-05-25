from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    seniority = models.CharField(max_length=100, blank=False)  # Стаж работы
    specialization = models.CharField(max_length=100, blank=False)  # Специализация
    photo = models.ImageField(upload_to='img/', default='img/def_photo.jpg')

    def __str__(self):
        return f"{self.name} ({self.specialization})"



class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Кто записался
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Доктор')  # К какому врачу
    date = models.DateField(verbose_name='Дата')  # Дата приёма
    time = models.TimeField(verbose_name='Время')  # Время приёма

    def __str__(self):
        return f"{self.user.username} → {self.doctor.name} ({self.date} {self.time})"