from django.shortcuts import render
# from property.models import modelname


def about(request):
    template = 'about/about.html'
    context = {}
    return render(request , template, context)