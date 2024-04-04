from django.shortcuts import render

# Create your views here.
def chicken(request):
    return render(request,'chicken.html')


def curd(request):
    return render(request,'curd.html')