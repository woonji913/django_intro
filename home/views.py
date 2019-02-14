from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse('Welcome to Django !')
    return render(request, 'index.html')
    
def dinner(request):
    dinner = ['스파게티', '돼지국밥', '순대국밥', '뼈해장국', '샤브샤브', '브리또', 
    '치킨', '피자', '엄마가 지어준 따끈한 밥', '아빠가 차려준 차가운 밥', '진라면', '미역국 라면', '짜빠게티',
    '짜장면', '볶음밥']
    menu = random.choice(dinner)
    return render(request, 'dinner.html', {'dinner': dinner, 'menu': menu})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, num):
    number = num**3
    return render(request, 'cube.html', {'num': num, 'number': number})
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data': data})
    
def user_new(request):
    # nickname, pwd
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    return render(request, 'user_create.html', {'nickname': nickname, 'password':password})

def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'template_example.html', {'my_list': my_list, 'my_sentence': my_sentence, 
                    'messages': messages, 'empty_list': empty_list, 'datetimenow': datetimenow})
   
