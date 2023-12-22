from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class TestSuite(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TestStep(models.Model):
    step = models.PositiveIntegerField()
    action = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255)

    def __str__(self):
        return str(self.step) + " - " + self.action


class TestCase(models.Model):
    STATE_CHOICES = [
        ('DESIGN', 'Design'),
        ('ACTIVE', 'Active'),
        ('CANCELLED', 'cancelled')
    ]

    PRIORITY_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Low')
    ]

    pre_conditions = models.TextField(blank=True, null=True)
    post_conditions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    title = models.TextField()
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    parameters = models.TextField(default="")
    test_steps = models.ManyToManyField(TestStep, related_name='test_cases')
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    estimated_time = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id) + " - " + self.title


class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.file.name


class DefectReplicationStep(models.Model):
    defect = models.ForeignKey('Defect', on_delete=models.CASCADE)
    attachment = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
    description = models.TextField()


class Defect(models.Model):
    STATUS_CHOICES = [
        ('OPENED', 'Opened'),
        ('IN_ANALISYS', 'In Analisys'),
        ('CLOSED', 'Closed'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    test_steps = models.ManyToManyField(DefectReplicationStep, related_name='defect_steps')


class Release(models.Model):
    starting_date = models.DateTimeField(auto_now_add=False)
    finishing_date = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # Casos de Testes selecionados para execução
    test_suite = models.ManyToManyField(TestCase, related_name='release_test_suite')

    def __str__(self):
        return "Release #" + str(self.id)


class TestCaseExecution(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('FAIL', 'Fail'),
    ]
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class TestStepExecution(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Success'),
        ('FAIL', 'Fail'),
    ]
    step = models.ForeignKey(TestStep, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField(default="")
    attachment = models.ForeignKey(UploadFile, on_delete=models.CASCADE)


