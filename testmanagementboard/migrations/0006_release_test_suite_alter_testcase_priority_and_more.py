# Generated by Django 4.1.5 on 2023-12-22 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testmanagementboard', '0005_defect_uploadfile_defectreplicationstep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='test_suite',
            field=models.ManyToManyField(related_name='release_test_suite', to='testmanagementboard.testcase'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='priority',
            field=models.CharField(choices=[('CRITICAL', 'Critical'), ('HIGH', 'High'), ('NORMAL', 'Normal'), ('LOW', 'Low')], max_length=10),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='state',
            field=models.CharField(choices=[('DESIGN', 'Design'), ('ACTIVE', 'Active'), ('CANCELLED', 'cancelled')], max_length=20),
        ),
        migrations.CreateModel(
            name='TestStepExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('SUCCESS', 'Success'), ('FAIL', 'Fail')], max_length=20)),
                ('description', models.TextField(default='')),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanagementboard.uploadfile')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanagementboard.teststep')),
            ],
        ),
        migrations.CreateModel(
            name='TestCaseExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('SUCCESS', 'Success'), ('FAIL', 'Fail')], max_length=20)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanagementboard.release')),
                ('test_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanagementboard.testcase')),
            ],
        ),
    ]
