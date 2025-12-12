from django.test import TestCase
from django.urls import reverse

from .models import Project, Skill

class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class ProjectSearchTests(TestCase):

    def setUp(self):
        self.skill = Skill.objects.create(name="Python")

        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            gitlab_url="https://example.com"
        )

        self.project.skills.add(self.skill)

    def test_search_by_skill(self):
        response = self.client.get(reverse("home"), {"q": "Python"})
        self.assertContains(response, "Test Project")


class CVPageTests(TestCase):

    def test_cv_page_status_code(self):
        response = self.client.get(reverse("cv"))
        self.assertEqual(response.status_code, 200)


class EmptySearchTests(TestCase):

    def test_search_returns_no_results(self):
        response = self.client.get(reverse("home"), {"q": "doesnotexist"})
        self.assertContains(response, "No projects available.")


class CVPdfLinkTests(TestCase):

    def test_cv_page_contains_pdf_link(self):
        response = self.client.get(reverse("cv"))
        self.assertContains(response, "cv.pdf")
