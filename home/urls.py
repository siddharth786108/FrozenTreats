from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("order", views.order, name='order'),
    path("payment", views.payment, name='payment'),
    path("Chocolate", views.Chocolate, name="Chocolate"),
    path("small_pack", views.small_pack, name='small_pack'),
    path("family_pack", views.family_pack, name='family_pack'),
    path("submit", views.submit, name='submit')
]
