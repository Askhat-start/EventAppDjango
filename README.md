# Система управления мероприятиями

EventApp - это веб-приложение для управления мероприятиями, позволяющая пользователям следущии функции:
- Просматривать события и мероприятия
- Просматривать информацию о каждом событии(дата,место,бронь и т.д.)
- Система аутентификации
- Бронировать места на мероприятия, отменять брони

### Технологии использованные в проекте
1. Django - полноценный Python Framework для создания как и frontend так и backend части веб приложения
2. HTML/CSS - язык разметки и язык каскадных стилей для оформления веб-страницы

## Процесс проектирования проекта
1. ### Проектирование базы данных:
   + Определение основных таблиц базы - Event, EventType, EventUser
   + Описание каждой модели. Пример: 
     ```python
     class Event(models.Model):
      title = models.CharField(verbose_name="Название мероприятия", max_length=255)
      organizer = models.CharField(verbose_name="Организаторы", max_length=255, default="Организация")
      description = models.TextField(verbose_name="Описание мероприятия")
      event_time = models.TimeField(default=datetime.time(12, 0))
      event_date = models.DateField(default=datetime.date.today)
      duration = models.FloatField(verbose_name="Продолжительность(в часах)")
      city = models.CharField(verbose_name="Город", max_length=255)
      location = models.CharField(verbose_name="Место проведения", max_length=255)
      seats_amount = models.IntegerField(verbose_name="Количество мест")
      event_type = models.ForeignKey(CategoryEvent, on_delete=models.PROTECT)
      available_seats = models.IntegerField(verbose_name="Доступное количество мест")
      photo = models.ImageField(upload_to='uploads/', default='uploads/default.png')```
2. ### Проектирвание навигации
   + Определение основных страниц приложения:
        + `main/` основные события, описание событий
        + `book/` бронирование, отмена бронирования, управления мероприятиями
        + `create_event/` создание новых мероприятий для админа сайта
        + `user_auth/` аутентификация(регистрация, вход в аккаунт)
   + Разработка структур URL адресов, например: 
   ```python 
   urlpatterns = [
    path('', views.main_events, name='main'),
    path('event/<int:event_id>', views.event_description, name='event_description'),
    path('event/<int:event_id>/take_part', booking_views.take_part, name='take_part'),
    path('create_event/', views.create_event, name='create_event')]```
   
3. ### Разработка представлений - view функции 
   + Создание представлений для каждой страницы (например, функция main для отображения событий на главной странице).
   + Интеграция системы аутентификации Django для обработки запросов пользователей.
   ```python 
   def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('/')
    register_form = CustomUserCreationForm
    return render(request, 'user_auth/register.html', context={'register_form': register_form})

    def user_login(request):
        if request.method == 'POST':
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')

        login_form = AuthenticationForm()
        return render(request=request, template_name='user_auth/login.html', context={'login_form': login_form})

    def user_logout(request):
        logout(request)
   ```
    + Использование CRUD
      + `create_event()` - CREATE - создания мероприятия на базе формы 
      + `description()` - READ - чтение данных объекта Event и вывод на экран
      + `take_par()` - UPDATE - при бронировании **изменяется** количество доступных мест у объекта Event
      + `delete_book()` - DELETE - удаление бронирования объекта EventUser
      
## Инструкция по настройке проекта

Перед началом настройки убедитесь, что у вас установлены следующие компоненты:

- Python (версия 3.0+)
- Django (установка с помощью pip: `pip install django`)

1. Клонируйте репозиторий проекта
2. В терминале откройте проект и введите: 
   `python manage.py migrate` для миграции базы данных Django
3. Для запуска проекта в терминале введите: `python manage.py runserver`
4. Перейдите по ссылке http://127.0.0.1:8000/ - это и есть веб-сайт проекта

## Компромиссы
1.Аутентификация - для аутентификации обязательным аспектом было наличие формы, так как это единственный input система для html страницы. 
После изучения ранее неизвестных мне функции Django, а именно `django.contrib.auth`, было принято решение использовать готовую форму `AuthenticationForm` для заполнения данных при регистрации пользователя
2.Для регистрации была использована идея из `django.contrib.auth` - создания собственной формы на базе готового `UserCreationForm`
```python
    class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
```
3.Возможные проблемы:
+ Низкая производительность базы данных. Фреймворк Django по умолчанию использует SQLLite базу данных что может сильно навредить оптимизации и скорости работы приложения
    + Решение: Установка современной версии PostgreSQL с целью повышения технологического уровня.
