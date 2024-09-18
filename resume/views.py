
from django.views.generic import TemplateView
from .models import CV, Certifications, Skills, Education, WorkExperience, Project

class CVPageView(TemplateView):
    template_name = 'resume/cv_page.html'  # Asegúrate de que la ruta sea correcta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cv'] = CV.objects.first()  # Suponiendo que solo hay un CV
        context['certifications'] = Certifications.objects.all()
        context['skills'] = Skills.objects.first()  # Solo uno, o ajusta si tienes varios
        context['education'] = Education.objects.all()
        context['work_experience'] = WorkExperience.objects.all()
        context['projects'] = Project.objects.all()
        return context
