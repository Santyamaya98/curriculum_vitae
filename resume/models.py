from django.db import models

class CV(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=50)  # Aumenté el tamaño para nombres más largos
    last_name = models.CharField(max_length=50)   # Aumenté el tamaño para apellidos más largos
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)

    # Professional Summary
    summary = models.TextField()  # Cambiado a TextField para un resumen más extenso

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Certifications(models.Model):
    # Origin of certificate
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, null=True)
    certificate_name = models.CharField(max_length=100)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    institution_name = models.CharField(max_length=100)
    institution_logo = models.ImageField(upload_to='institution_logos/', blank=True, null=True)

    def __str__(self):
        return self.certificate_name


class Skills(models.Model):
    # Many-to-many relationship with Language

    cv = models.ForeignKey(CV, on_delete=models.CASCADE, null=True)
    # Other skill categories
    soft_skills = models.CharField(max_length=200)
    technical_skills = models.TextField()

    def __str__(self):
        return f'Skills: {self.soft_skills}'


class Education(models.Model):

    cv = models.ForeignKey(CV, on_delete=models.CASCADE, null=True)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.degree} from {self.institution}'

class WorkExperience(models.Model):

    cv = models.ForeignKey(CV,  on_delete=models.CASCADE, null=True)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()

    def __str__(self):
        return f'{self.job_title} at {self.company}'

class Project(models.Model):

    cv = models.ForeignKey(CV, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

