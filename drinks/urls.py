from django.urls import path
from drinks.views import *
app_name='drinks'

urlpatterns=[
    path('bindu/',bindu,name='bindu'),
    path('maaza/',maaza,name='maaza'),
]