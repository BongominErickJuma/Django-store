from django.urls import path
from .views import sayHello

urlpatterns = [
    path("hello/", sayHello, name="say_hello"), # New URL pattern   
]