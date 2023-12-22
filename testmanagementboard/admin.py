from django.contrib import admin

# Register your models here.
from .models import Project, Release, TestCase, TestStep, DefectReplicationStep, UploadFile, Defect, \
    TestCaseExecution, TestStepExecution, Parameter

admin.site.register(Project)
admin.site.register(Release)
admin.site.register(TestCase)
admin.site.register(TestStep)

admin.site.register(DefectReplicationStep)
admin.site.register(UploadFile)
admin.site.register(Defect)

admin.site.register(TestCaseExecution)
admin.site.register(TestStepExecution)

admin.site.register(Parameter)

