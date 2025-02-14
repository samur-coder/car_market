from tkinter.font import names

from django.urls import path

from .views import home, about, detail,car,contact,service,team, testimonial, booking
urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("detail", detail, name="detail"),
    path("car", car, name="car"),
    path("booking", booking, name="booking"),
    path("contact", contact, name="contact"),
    path("service", service, name="service"),
    path("team", team, name="team"),
    path("testimonal", testimonial, name="testimonal")
]