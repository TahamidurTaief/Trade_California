from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path("connect/<str:role>/", views.connect, name="connect"),
]
