from django.shortcuts import render, redirect

from .form import ContactForm
from .models import Sold_car, our_servise, Contact
import random


def home(request):
    contact = Contact.objects.all().last()
    our = our_servise.objects.all()
    sold = Sold_car.objects.all()
    a = list(sold)
    car_first = random.choice(a)
    while True:
        car_last = random.choice(a)
        if car_first!=car_last:
            break

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    context = {
        "form":form,
        "contact":contact,
        "sold":sold,
        "our":our,
        "car_first":car_first,
        "car_last":car_last,
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def detail(request):
    return render(request, "detail.html")

def car(request):
    return render(request, "car.html")

def contact(request):
    return render(request, "contact.html")


def service(request):
    return render(request, "service.html")

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")

def booking(request):
    return render(request, "booking.html")