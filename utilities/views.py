from django.shortcuts import render
from datetime import datetime, date
import requests
import json
import os

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    dday = datetime(2019, 2, 28) - datetime.now()
    return render(request, 'utilities/bye.html', {'dday': dday})
    
def graduation(request):
    mire = datetime(2019, 5, 28)
    now = datetime(2019, 2, 14)
    delta_day = mire- now
    return render(request, 'utilities/graduation.html', {'delta_day': delta_day})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')

def today(request):
    key = os.getenv("KEY")
    url_req = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID={key}'
    
    res = requests.get(url_req).json()
    weather = res["weather"][0]["description"]
    return render(request, 'utilities/today.html', {'weather': weather})
    
def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'fonts': fonts})
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    req = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'req': req})
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    return render(request, 'utilities/translated.html')