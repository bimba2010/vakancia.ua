# Generated by Django 5.1.4 on 2025-04-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_vacancy_description_alter_vacancy_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='education',
            field=models.CharField(choices=[('Tehno', 'Техно'), ('Dergavna', 'Державна робота')], default='GeneralSecondaryEducation', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='kategoria',
            field=models.TextField(choices=[('Tehno', 'Техно'), ('Dergavna', 'Державна робота')], default='Tehno', max_length=1000000, null=True),
        ),
    ]
