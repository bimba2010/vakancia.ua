# Generated by Django 5.1.4 on 2025-02-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_resume_resumekategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='mainvacancy',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
