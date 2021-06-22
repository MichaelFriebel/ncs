from django.shortcuts import render
# from home.models import modelname

def home(request):
    template = 'home/home.html'
    context = {}
    return render(request , template , context)