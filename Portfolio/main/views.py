from django.shortcuts import render
from django.db.models import Q
from .models import Project, Skill


def home(request):
    query = request.GET.get("q", "")

    projects = Project.objects.all()

    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(skills__name__icontains=query)
        ).distinct()

    skills = Skill.objects.all()

    return render(request, "main/home.html", {
        "projects": projects,
        "skills": skills,
    })


def cv(request):
    return render(request, "main/cv.html")

