from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView

from app.Forms import VacancyForm, ResumeForm
from app.models import Vacancy, Resume, Kategoria
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VakancyList.html'  # Шаблон, який буде використовуватися для відображення
    context_object_name = 'vacancys'  # Це ім'я змінної в шаблоні, в яку будуть передаватися елементи

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyDetail.html'  # Шаблон для відображення детальної інформації
    context_object_name = 'vacancy'  # Це ім'я змінної в шаблоні, в яку буде передаватися конкретна вакансія

class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyCreate.html'  # Шаблон для створення вакансії
    form_class = VacancyForm  # Форма для створення вакансії
    success_url = reverse_lazy('vacancy_list')  # Куди перенаправляти після успішного створення
    login_url = '/login/'  # Вказуємо шлях до сторінки входу

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Автоматично прив'язуємo автора вакансії
        return super().form_valid(form)

class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyConfirmDelete.html'  # Шаблон для підтвердження видалення
    success_url = reverse_lazy('vacancy_list')  # Після видалення перенаправляємо на список вакансій



class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'vacancyonline/ResumeCreate.html'  # Шаблон для створення резюме
    success_url = reverse_lazy('resume_list')  # Перенаправляємо після успішного створення на список резюме
    login_url = '/login/'  # Вказуємо шлях до сторінки входу

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Автоматично прив'язуємо користувача до резюме
        return super().form_valid(form)

class ResumeListView(ListView):
    model = Resume
    template_name = 'vacancyonline/ResumeList.html'  # Шаблон для відображення списку резюме
    context_object_name = 'resumes'  # Ім'я змінної для списку резюме в шаблоні


class AboutUsView(TemplateView):
    template_name = 'vacancyonline/about_us.html'  # Вказуємо шаблон для сторінки "Про нас"


class ResumeDeleteView(DeleteView):
    model = Resume
    template_name = 'vacancyonline/ResumeConfirmDelete.html'
    success_url = reverse_lazy('resume_list')



class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'vacancyonline/ResumeDetail.html'  # Шаблон для відображення детальної інформації
    context_object_name = 'resume'  # Це ім'я змінної в шаблоні, в яку буде передаватися конкретна вакансія


# Представлення для входу
class VacancyLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'vacancyonline/VacancyLogin.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('vacancy_list')  # Перенаправлення на список вакансій після входу
        return render(request, 'vacancyonline/VacancyLogin.html', {'form': form})


# Представлення для реєстрації
class VacancySignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'vacancyonline/VacancySignUp.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')  # Перенаправлення після успішної реєстрації
        return render(request, 'vacancyonline/VacancySignUp.html', {'form': form})



class VacancyKategoriaView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyKategoria.html'  # Шаблон, який буде використовуватися для відображення
    context_object_name = 'vacancykategoria'  # Це ім'я змінної в шаблоні, в яку будуть передаватися елементи



class VacancyTehnoView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyTehno.html'
    context_object_name = 'vacancytehno'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(kategoria='Tehno')


class VacancyDergavnaView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyDergavna.html'
    context_object_name = 'vacancydergavna'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(kategoria='Dergavna')


class ResumeKategoriaView(ListView):
    model = Resume
    template_name = 'vacancyonline/resumekategoria.html'
    context_object_name = 'kategoria'


class ResumeProfessionalExperienceView(ListView):
    model = Resume
    template_name = 'vacancyonline/resumeprofessionalexperience.html'
    context_object_name = 'professionalexperience'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Resume.objects.filter(resumekategoria='ProfessionalExperience')


class ResumeProjectsView(ListView):
    model = Resume
    template_name = 'vacancyonline/resumeprojects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Resume.objects.filter(resumekategoria='Projects')


class VacancyCityView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyCity.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        # Отримуємо параметр з URL-шляху
        city_name = self.kwargs.get('vacancycity')

        if city_name:
            # Фільтруємо вакансії за містом
            return Vacancy.objects.filter(city=city_name)
        else:
            # Якщо параметр відсутній, повертаємо всі вакансії
            return Vacancy.objects.all()



class VacancyVinnytsiaView(ListView):
        model = Vacancy
        template_name = 'vacancyonline/VacancyVinnytsia.html'
        context_object_name = 'vacancyvinnytsia'

        def get_queryset(self):
            # Отримуємо категорію з URL і фільтруємо пости по категорії
            return Vacancy.objects.filter(city='Vinnytsia')


class VacancyPoltavaView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyPoltava.html'
    context_object_name = 'vacancypoltava'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Poltava')



class VacancyChernivtsiView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyChernivtsi.html'
    context_object_name = 'vacancychernivtsi'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Chernivtsi')



class VacancyCherkasyView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyCherkasy.html'
    context_object_name = 'vacancycherkasy'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Cherkasy')


class VacancyZaporizhzhiaView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyZaporizhzhia.html'
    context_object_name = 'vacancyzaporizhzhia'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Zaporizhzhia')



class VacancyDnipropetrovskView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyDnipropetrovsk.html'
    context_object_name = 'vacancydnipropetrovsk'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Dnipropetrovsk')




class VacancyKharkivView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyKharkiv.html'
    context_object_name = 'vacancykharkiv'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Kharkiv')





class VacancyOdessaView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyOdessa.html'
    context_object_name = 'vacancyodessa'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Odessa')





class VacancyLvivView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyLviv.html'
    context_object_name = 'vacancylviv'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Lviv')





class VacancyKyivView(ListView):
    model = Vacancy
    template_name = 'vacancyonline/VacancyKyiv.html'
    context_object_name = 'vacancykyiv'

    def get_queryset(self):
        # Отримуємо категорію з URL і фільтруємо пости по категорії
        return Vacancy.objects.filter(city='Kyiv')



class VacancyLogOutView(ListView):
    template_name = 'vacancyonline/VacancyLogOut.html'
    context_object_name = 'logout'



