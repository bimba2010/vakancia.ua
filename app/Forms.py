from django import forms
from .models import Vacancy, Resume


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'city', 'salary', 'education', 'description', 'kategoria', 'mainvacancy',]  # Подаємо поля для вакансії

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'resume', 'resumekategoria']  # Подаємо поля для введення