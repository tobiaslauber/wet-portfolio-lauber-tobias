from django.shortcuts import render
from .models import Project, Skill


def home(request):
    # Alle Projekte und Skills aus der Datenbank holen
    projects = Project.objects.all()
    skills = Skill.objects.all()

    # An das Template schicken
    return render(request, "main/home.html", {
        "projects": projects,
        "skills": skills,
    })


def cv(request):
    return render(request, "main/cv.html")
