from django.contrib import admin
from .models import CV, Certifications, Language, Skills, Formation, Education, WorkExperience, Project

admin.site.register(CV)
admin.site.register(Certifications)
admin.site.register(Language)
admin.site.register(Skills)
admin.site.register(Formation)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Project)
