


from django.contrib import admin
from django.urls import path
from myapp import views



urlpatterns = [
    path('welcome',views.home),
    path('about',views.about),
    path('contact',views.contact)
]