from django.shortcuts import render, redirect
from .models import City, Weather
from .forms import WeatherForm
import requests

def index(request):
    city = City.objects.all
    form = WeatherForm(request.POST)
    if form.is_valid():
        weather = form.save()
        weather.save()
        return redirect('index')

    key = 'f6c769fcada5855c940848a03b4e1792'
    cheb = 'Cheboksary'
    url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    responce = requests.get(url.format(cheb, key)).json()
    cheb = {'city': cheb,
             'temp': responce['main']['temp'],
             'icon': responce['weather'][0]['icon'],
             }

    city_weather = Weather.objects.all()
    for item in city_weather:
        key = 'f6c769fcada5855c940848a03b4e1792'
        id_city = item.city_id
        city = City.objects.get(id=id_city)
        url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
        responce = requests.get(url.format(city, key)).json()
        res = {
            'city': city,
            'temp': responce['main']['temp'],
            'icon': responce['weather'][0]['icon'],
            }
    if len(city_weather) > 0: 
        contex = {'info': res, 'cheb': cheb, 'form': form, 'city_weather': city_weather}
    else:
        contex = {'cheb': cheb, 'form': form, 'city_weather': city_weather}

    return render(request, 'weather/index.html', contex)