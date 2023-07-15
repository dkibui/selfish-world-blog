from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("team/", views.team, name="team"),
    path("service/", views.service, name="service"),
    path("contact/", views.contact, name="contact"),
]
