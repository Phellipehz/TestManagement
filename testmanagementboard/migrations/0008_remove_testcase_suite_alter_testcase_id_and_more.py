# Generated by Django 4.1.5 on 2023-12-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmanagementboard', '0007_remove_defect_project_defect_release'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='suite',
        ),
        migrations.AlterField(
            model_name='testcase',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='title',
            field=models.TextField(default=None),
        ),
        migrations.DeleteModel(
            name='TestSuite',
        ),
    ]
