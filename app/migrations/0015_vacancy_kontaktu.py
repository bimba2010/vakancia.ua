# Generated by Django 5.1.4 on 2025-03-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_resume_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='kontaktu',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
