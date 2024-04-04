from django.urls import path
from food.views import *
app_name='food'

urlpatterns=[
    path('chicken/',chicken,name='chicken'),
    path('curd/',curd,name='curd'),
]