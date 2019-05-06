from django.contrib import admin
from .models import Problem, Submission , TestCase

# Register your models here.


admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(TestCase)
