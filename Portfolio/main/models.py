from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    gitlab_url = models.URLField()

    # Many-to-Many Beziehung
    skills = models.ManyToManyField(Skill, related_name="projects")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
