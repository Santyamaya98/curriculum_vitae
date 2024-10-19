from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import CV, Certifications, Skills, Education, WorkExperience, Project
from django.urls import reverse

class CVModelTests(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            summary="A professional software developer."
        )

    def test_cv_str(self):
        self.assertEqual(str(self.cv), "John Doe")

    def test_certifications_str(self):
        cert = Certifications.objects.create(
            cv=self.cv,
            certificate_name="Python Certification",
            institution_name="Udemy"
        )
        self.assertEqual(str(cert), "Python Certification")

    def test_skills_str(self):
        skills = Skills.objects.create(
            cv=self.cv,
            soft_skills="Communication",
            technical_skills="Python, Django"
        )
        self.assertEqual(str(skills), "Skills: Communication")

class CVViewTests(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            summary="Experienced project manager."
        )
        self.valid_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'summary': 'Experienced project manager.'
        }

    def test_create_cv_view_get(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)

    def test_create_cv_view_post_valid_data(self):
        response = self.client.post(reverse('add'), self.valid_data)
        self.assertRedirects(response, reverse('success'))  # Asegúrate de ajustar esto según tu lógica

    def test_create_cv_view_post_invalid_data(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = ''  # Email vacío para invalidar
        response = self.client.post(reverse('add'), invalid_data)
        self.assertEqual(response.status_code, 400)  # Ajusta según tu manejo de errores

# Pruebas adicionales para las vistas de certificaciones, educación, experiencia laboral y proyectos
class CertificationsViewTests(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alice.smith@example.com",
            summary="Data scientist."
        )
        self.cert_data = {
            'cv': self.cv.id,
            'certificate_name': 'Data Science Certification',
            'institution_name': 'Coursera'
        }

    def test_create_certification(self):
        response = self.client.post(reverse('add_certification'), self.cert_data)
        self.assertEqual(response.status_code, 302)  # Verifica redirección después de una creación exitosa

# Y así sucesivamente para los otros modelos
