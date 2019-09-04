# now-django-example/example_app/urls.py
from django.urls import path
from example_app.views import index,dlxl
urlpatterns = [
    path('', index),
    path('dlxl', dlxl),

]