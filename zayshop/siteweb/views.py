from django.shortcuts import render, redirect
from . import models 


# Create your views here.
def index(request):
    slides = models.Slider.objects.filter(status=True)
    return render(request, 'index.html', locals())


def about(request):
    abouts = models.About.objects.filter(status=True)
    marques =models.Marque.objects.
    return render(request, 'about.html', locals())

def shop(request):
    return render(request, 'shop.html')

def shopsingle(request):
    return render(request, 'shop-single.html')

def contact(request):
    return render(request, 'contact.html')

def newsletterpost(request):
    newemail = request.POST.get("email")
    retour = request.META.get("HTTP_REFERER") #rediriger lutilisateur sur sa page ou il s inscrit
    new = models.Newsletter() # pour enregister le email dans la base de donees
    new.email = newemail
    new.save()
    return redirect(retour, "index")