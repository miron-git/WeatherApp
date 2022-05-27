from django import forms
from .models import City, Weather

class WeatherForm(forms.ModelForm):

    class Meta:
        model = Weather
        fields = ('city',)