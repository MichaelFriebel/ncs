from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
# from reservation.dates import available_dates

# def index(request):
    # template = 'home/home.html'
    # context = {
    #     'available_dates': available_dates,
    # }
    # return render(request, 'pages/index.html')


class IndexView(generic.TemplateView):
    template_name = "pages/index.html"

    def dispatch(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

class AboutView(generic.TemplateView):
    template_name = "pages/about.html"

    def dispatch(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

class ContactView(generic.TemplateView):
    template_name = "pages/contact.html"

    def dispatch(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)

class GalleryView(generic.TemplateView):
    template_name = "pages/gallery.html"

    def dispatch(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)



# def about(request):
#     # template = 'home/home.html'
#     return render(request, 'pages/about.html')

# def contact(request):
#     template = 'pages/contact.html'
#     # context = {}
#     return render(request, template)

# def gallery(request):
#     template = 'pages/gallery.html'
#     # context = {}
#     return render(request , template)