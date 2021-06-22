from django.shortcuts import render
# from property.models import modelname


def contact(request):
    template = 'contact/contact.html'
    context = {}
    return render(request , template, context)