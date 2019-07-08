from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'a': 2}
    for i in range(2):
        print("Arun")
    return render(request, 'home/index1.html', {'b':3})
