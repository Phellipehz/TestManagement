from django.contrib import admin

# Register your models here.
from .models import Project, Release, TestCase, TestStep, TestSuite, DefectReplicationStep, UploadFile, Defect, \
    TestCaseExecution, TestStepExecution

admin.site.register(Project)
admin.site.register(Release)
admin.site.register(TestCase)
admin.site.register(TestStep)
admin.site.register(TestSuite)

admin.site.register(DefectReplicationStep)
admin.site.register(UploadFile)
admin.site.register(Defect)

admin.site.register(TestCaseExecution)
admin.site.register(TestStepExecution)