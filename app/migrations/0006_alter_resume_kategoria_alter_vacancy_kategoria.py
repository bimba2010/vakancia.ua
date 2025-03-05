# Generated by Django 5.1.4 on 2025-02-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_vacancy_kategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='kategoria',
            field=models.TextField(choices=[('Tehno', 'Техно'), ('Dergavna', 'Державна робота')], default='Tehno', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='kategoria',
            field=models.TextField(choices=[('Tehno', 'Техно'), ('Dergavna', 'Державна робота')], default='Tehno', max_length=10, null=True),
        ),
    ]
