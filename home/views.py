from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django !')
    
def dinner(request):
    dinner = ['스파게티', '돼지국밥', '순대국밥', '뼈해장국', '샤브샤브', '브리또', 
    '치킨', '피자', '엄마가 지어준 따끈한 밥', '아빠가 차려준 차가운 밥', '진라면', '미역국 라면', '짜빠게티',
    '짜장면', '볶음밥']
    menu = random.choice(dinner)
    return render(request, 'dinner.html', {'dinner': dinner, 'menu': menu})