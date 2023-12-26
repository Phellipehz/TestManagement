from django.contrib import admin

# Register your models here.
from .models import Project, TestExecution, TestCase, TestStep, UploadFile, \
    TestCaseExecution, TestStepExecution, Parameter, TestSuite, TestPlan

admin.site.register(Project)
admin.site.register(TestExecution)
admin.site.register(TestCase)
admin.site.register(TestStep)
admin.site.register(TestSuite)
admin.site.register(TestPlan)

admin.site.register(UploadFile)

admin.site.register(TestCaseExecution)
admin.site.register(TestStepExecution)

admin.site.register(Parameter)

