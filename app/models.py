from enum import Enum

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField

class Kategoria(Enum):
    Tehno =  'Техно'
    Dergavna = 'Державна робота'


class VacancyCity(Enum):
    Kyiv = 'Київ'
    Lviv = 'Львів'
    Odessa = 'Одеса'
    Kharkiv = 'Харків'
    Dnipropetrovsk = 'Дніпро'
    Zaporizhzhia = 'Запоріжжя'
    Cherkasy = 'Черкаси'
    Chernivtsi = 'Чернівці'
    Poltava = 'Полтава'
    Vinnytsia = 'Вінниця '



class ResumeKategoria(Enum):
    ProfessionalExperience = 'Професійний досвід'
    Projects = 'Проекти'






class Vacancy(models.Model):
    title = models.CharField(max_length= 100000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(
        max_length= 100000,
        choices = [(tag.name, tag.value) for tag in VacancyCity],
        default = VacancyCity.Lviv.name,)  # Встановіть стандартний статус)

    salary = models.DecimalField(max_digits= 1000 , decimal_places= 2)
    education = models.CharField(max_length= 1000000)
    description = models.CharField(max_length= 100000)
    kategoria = models.TextField(null = True,
        max_length=10,
        choices=[(tag.name, tag.value) for tag in Kategoria],
        default=Kategoria.Tehno.name,)# Встановіть стандартний статус)
    mainvacancy = models.CharField(null = True, max_length= 100000)
    kontaktu = models.CharField(null = True, max_length= 100000)




class Resume(models.Model):
    title = models.CharField(max_length=255)  # Назва резюме
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Користувач, який створив резюме
    resume = models.TextField(max_length= 10000)  # Текст самого резюме
    resumekategoria = models.TextField(null = True,

                                 choices=[(tag.name, tag.value) for tag in ResumeKategoria],
                                 default=ResumeKategoria.Projects.name, )  # Встановіть стандартний статус)

    resumekontaktu = models.CharField(null=True, max_length=100000)



    def __str__(self):
        return self.title
