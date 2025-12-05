from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def cv(request):
    return render(request, "main/cv.html")


