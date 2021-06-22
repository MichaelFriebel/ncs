from django.shortcuts import render
# from property.models import modelname


def gallery(request):
    template = 'gallery/gallery.html'
    context = {}
    return render(request , template, context)