from django import forms
from .models import Appointment
import datetime
from .models import Doctor
from datetime import datetime, time, timedelta

class AppointmentForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label="Доктор")
    date = forms.DateField(widget=forms.SelectDateWidget(), label="Дата")
    time = forms.ChoiceField(choices=[], widget=forms.Select(), label="Время")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Генерация временных слотов от 08:00 до 20:00 с шагом 30 минут
        time_slots = []
        start_time = time(8, 0)  # 08:00
        end_time = time(20, 0)  # 20:00
        interval = timedelta(minutes=30)

        current_time = start_time
        while current_time <= end_time:
            time_str = current_time.strftime("%H:%M")
            time_slots.append((time_str, time_str))
            current_time = (datetime.combine(datetime.today(), current_time) + interval).time()

        self.fields['time'].choices = time_slots

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if Appointment.objects.filter(doctor=doctor, date=date, time=time).exists():
            raise forms.ValidationError("Выбранное время уже занято!")
        return cleaned_data