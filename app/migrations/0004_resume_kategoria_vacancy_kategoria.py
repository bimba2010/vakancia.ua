# Generated by Django 5.1.4 on 2025-02-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='kategoria',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='kategoria',
            field=models.TextField(null=True),
        ),
    ]
