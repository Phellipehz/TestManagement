from django.db import models


# OK
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# OK
class TestPlan(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    test_suites = models.ManyToManyField('TestSuite', related_name='test_plan_suites', blank=True, null=True)

    def __str__(self):
        return self.title


# OK
class TestSuite(models.Model):
    PRIORITY_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Low')
    ]

    STATE_CHOICES = [
        ('DESIGN', 'Design'),
        ('ACTIVE', 'Active'),
        ('CANCELLED', 'Cancelled')
    ]

    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    pre_conditions = models.TextField(blank=True, null=True)
    post_conditions = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='DESIGN')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title


# OK
class TestCase(models.Model):
    STATE_CHOICES = [
        ('DESIGN', 'Design'),
        ('ACTIVE', 'Active'),
        ('CANCELLED', 'Cancelled')
    ]

    PRIORITY_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Low')
    ]

    BASE_CHOICES = [
        ('BASE', 'Base'),
        ('ALTERNATIVE', 'Alternative'),
        ('ERROR', 'Error')
    ]

    id = models.AutoField(primary_key=True)
    suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField()
    description = models.TextField()
    pre_conditions = models.TextField(blank=True, null=True)
    post_conditions = models.TextField(blank=True, null=True)
    test_steps = models.ManyToManyField('TestStep', related_name='test_cases')
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    type = models.CharField(max_length=25, choices=BASE_CHOICES, default="Base")
    previous_version = models.ForeignKey('TestCase', on_delete=models.CASCADE, blank=True, null=True)
    estimated_time = models.PositiveIntegerField(default=0)
    parameters = models.ManyToManyField('Parameter', related_name='test_case_parameters', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    attachments = models.ForeignKey('UploadFile', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


# OK
class TestStep(models.Model):
    step = models.PositiveIntegerField()
    action = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255)

    def __str__(self):
        return str(self.step) + " - " + self.action


######################################################

# OK
class TestExecution(models.Model):
    id = models.AutoField(primary_key=True)
    version = models.TextField(default="")
    starting_date = models.DateTimeField(auto_now_add=True)
    finishing_date = models.DateTimeField(auto_now_add=False)
    testplan = models.ForeignKey(TestPlan, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "Release #" + str(self.id)


class TestCaseExecution(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('FAIL', 'Fail'),
        ('ON_GOING', 'On Going'),
    ]

    id = models.AutoField(primary_key=True)
    release = models.ForeignKey(TestExecution, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class TestStepExecution(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('FAIL', 'Fail'),
        ('ON_GOING', 'On Going'),
    ]
    step = models.ForeignKey('TestStep', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # defect = models.ForeignKey('Defect', on_delete=models.CASCADE, blank=True, null=True)


######################################################

# OK
class Parameter(models.Model):
    key = models.TextField()
    value = models.TextField()
    attachments = models.ForeignKey('UploadFile', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.key + " " + self.value


# OK
class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.file.name
