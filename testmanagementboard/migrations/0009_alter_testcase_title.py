# Generated by Django 4.1.5 on 2023-12-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmanagementboard', '0008_remove_testcase_suite_alter_testcase_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
