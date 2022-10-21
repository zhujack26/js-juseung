import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    foods =['apple']
    info = {
        'name': 'Alice'
    }
    context = {
        'foods': foods,
        'info' : info,
    }
    return render(request, 'articles/greeting.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def dinner(request):
    foods = ['족발', '햄버거']
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'articles/dinner.html', context)

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)