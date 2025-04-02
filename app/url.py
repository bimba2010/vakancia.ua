from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from .views import VacancyListView, VacancyDetailView, VacancyCreateView, VacancyDeleteView, ResumeCreateView, \
    ResumeListView, AboutUsView, ResumeDeleteView, ResumeDetailView, VacancyLoginView, VacancySignUpView, \
    VacancyKategoriaView, VacancyTehnoView, VacancyDergavnaView, ResumeKategoriaView, ResumeProjectsView, \
    ResumeProfessionalExperienceView, VacancyCityView, VacancyKyivView, VacancyLvivView, VacancyOdessaView, \
    VacancyKharkivView, VacancyDnipropetrovskView, VacancyZaporizhzhiaView, VacancyCherkasyView, VacancyChernivtsiView, \
    VacancyPoltavaView, VacancyVinnytsiaView, VacancyLogOutView, GeneralSecondaryEducationView, HigherEducationView, \
    VocationalEducationView, VacancyEducationVieww

urlpatterns = [
    path('vacancy_list/', VacancyListView.as_view(), name = 'vacancy'),
    path('', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),  # Маршрут для створення вакансії
    path('vacancy/', VacancyListView.as_view(), name='vacancy_list'),  # Маршрут для списку вакансій
    path('vacancy/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/delete/<int:pk>/', VacancyDeleteView.as_view(), name='vacancy_delete'),# Маршрут для видалення вакансії
    path('resume/create/', ResumeCreateView.as_view(), name='resume_create'),
    path('resume/', ResumeListView.as_view(), name='resume_list'),  # Це для відображення списку резюме# Інші маршрути...
    path('vacancy_list/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/delete/<int:pk>/', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('resume/create/', ResumeCreateView.as_view(), name='resume_create'),
    path('resume/', ResumeListView.as_view(), name='resume_list'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),  # Додаємо маршрут для сторінки "Про нас"
    path('resume/delete/<int:pk>',ResumeDeleteView.as_view(), name='resume_delete'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
    path('login/', VacancyLoginView.as_view(), name='login'),  # Шлях для входу
    path('signup/', VacancySignUpView.as_view(), name='signup'),  # Шлях для реєстрації
    path('kategoria/',VacancyKategoriaView.as_view(), name = 'kategoria'),
    path('tehno/',VacancyTehnoView.as_view(), name = 'tehno'),
    path('dergavna/', VacancyDergavnaView.as_view(), name='dergavna'),
    path('resumekategoria/', ResumeKategoriaView.as_view(), name='resumekategoria'),
    path('professionalexperience/', ResumeProfessionalExperienceView.as_view(), name='professionalexperience'),
    path('projects/', ResumeProjectsView.as_view(), name='projects'),
    path('VacancyEducation/', VacancyEducationVieww.as_view(), name='VacancyEducation'),




    path('city/<str:vacancycity>/', VacancyCityView.as_view(), name='vacancy_city'),

    path('vacancyvinnytsia/', VacancyVinnytsiaView.as_view(), name='vacancyvinnytsia'),

    path('vacancypoltava/', VacancyPoltavaView.as_view(), name='vacancypoltava'),

    path('vacancychernivtsi/', VacancyChernivtsiView.as_view(), name='vacancychernivtsi'),

    path('vacancycherkasy/', VacancyCherkasyView.as_view(), name='vacancycherkasy'),

    path('vacancyzaporizhzhia/', VacancyZaporizhzhiaView.as_view(), name='vacancyzaporizhzhia'),

    path('vacancydnipropetrovsk/', VacancyDnipropetrovskView.as_view(), name='vacancydnipropetrovsk'),

    path('vacancykharkiv/', VacancyKharkivView.as_view(), name='vacancykharkiv'),

    path('vacancyodessa/', VacancyOdessaView.as_view(), name='vacancyodessa'),

    path('vacancylviv/', VacancyLvivView.as_view(), name='vacancylviv'),

    path('vacancykyiv/', VacancyKyivView.as_view(), name='vacancykyiv'),

    path('logout/', LogoutView.as_view(next_page='vacancy'), name='logout'),


    path('GeneralSecondaryEducation/', GeneralSecondaryEducationView.as_view(), name='GeneralSecondaryEducation'),

    path('HigherEducation/', HigherEducationView.as_view(), name='HigherEducation'),

    path('VocationalEducation/', VocationalEducationView.as_view(), name='VocationalEducation'),
]
