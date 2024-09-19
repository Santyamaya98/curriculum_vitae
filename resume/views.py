
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.forms import modelformset_factory

from .models import CV, Certifications, Skills, Education, WorkExperience, Project
from .forms import CVForm, CertificationsForm, SkillsForm, EducationForm, WorkExperienceForm, ProjectForm



CertificationsFormSet = modelformset_factory(Certifications, form=CertificationsForm, extra=1)


    
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

class CVCreateView(View):
    def get(self, request):
        cv_form = CVForm()
        certifications_formset = CertificationsFormSet(queryset=Certifications.objects.none())
        skills_form = SkillsForm()
        education_form = EducationForm()
        work_experience_form = WorkExperienceForm()
        project_form = ProjectForm()

        context = {
            'cv_form': cv_form,
            'certifications_formset': certifications_formset,
            'skills_form': skills_form,
            'education_form': education_form,
            'work_experience_form': work_experience_form,
            'project_form': project_form,
        }
        return render(request, 'resume/cv_form.html', context)

    def post(self, request):
        cv_form = CVForm(request.POST, request.FILES)
        certifications_formset = CertificationsFormSet(request.POST, request.FILES)
        skills_form = SkillsForm(request.POST)
        education_form = EducationForm(request.POST)
        work_experience_form = WorkExperienceForm(request.POST)
        project_form = ProjectForm(request.POST)

        if (cv_form.is_valid() and
            certifications_formset.is_valid() and
            skills_form.is_valid() and
            education_form.is_valid() and
            work_experience_form.is_valid() and
            project_form.is_valid()):
            
            cv = cv_form.save()
            for form in certifications_formset:
                certification = form.save(commit=False)
                certification.cv = cv  # Link the certification to the CV
                certification.save()

            # Save other forms
            skills = skills_form.save(commit=False)
            skills.save()
            education = education_form.save(commit=False)
            education.save()
            work_experience = work_experience_form.save(commit=False)
            work_experience.save()
            project = project_form.save(commit=False)
            project.save()

            return redirect('cv_success')

        context = {
            'cv_form': cv_form,
            'certifications_formset': certifications_formset,
            'skills_form': skills_form,
            'education_form': education_form,
            'work_experience_form': work_experience_form,
            'project_form': project_form,
        }
        return render(request, 'resume/cv_form.html', context)