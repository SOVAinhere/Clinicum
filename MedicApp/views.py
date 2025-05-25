from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView

from MedicApp.models import Doctor

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
import datetime


# Create your views here.
def index(request):
    context = {
        "title": 'Главная страница'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'О клинике'})

class Doctors(ListView):
    model = Doctor
    template_name = 'doctors.html'
    context_object_name = 'doctors'
    extra_context = {
        'title': 'Врачи'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Врачи'
        return context

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointments_list')  # Страница с записями
    else:
        form = AppointmentForm()

    return render(request, 'appointment_form.html', {'form': form})


def get_available_slots(doctor, date):
    start_time = datetime.time(8, 0)  # 08:00
    end_time = datetime.time(20, 0)  # 20:00
    interval = datetime.timedelta(minutes=30)

    existing_appointments = Appointment.objects.filter(doctor=doctor, date=date).values_list('time', flat=True)

    slots = []
    current_time = datetime.datetime.combine(datetime.date.today(), start_time)

    while current_time.time() < end_time:
        if current_time.time() not in existing_appointments:
            slots.append(current_time.time())
        current_time += interval

    return slots


def contact(request):
    return render(request, 'contact.html', context={
        'title':'Контакты'
    })


