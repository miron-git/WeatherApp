from django.shortcuts import render
from .models import City
import requests

def index(request):
    key = 'f6c769fcada5855c940848a03b4e1792'
    city = City.objects.all
    url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    responce = requests.get(url.format(city, key)).json()
    res = {'city': city,
            'temp': responce['main']['temp'],
            'icon': responce['weather'][0]['icon'],
            }
    print(res)
    contex = {'info': res}
    return render(request, 'weather/index.html', contex)