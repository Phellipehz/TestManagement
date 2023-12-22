# Generated by Django 4.1.5 on 2023-12-22 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testmanagementboard', '0004_rename_teststeps_teststep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('OPENED', 'Opened'), ('IN_ANALISYS', 'In Analisys'), ('CLOSED', 'Closed')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanagementboard.project')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='DefectReplicationStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanagementboard.uploadfile')),
                ('defect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanagementboard.defect')),
            ],
        ),
        migrations.AddField(
            model_name='defect',
            name='test_steps',
            field=models.ManyToManyField(related_name='defect_steps', to='testmanagementboard.defectreplicationstep'),
        ),
    ]