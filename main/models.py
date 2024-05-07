from django.db import models
import datetime


class CategoryEvent(models.Model):
    title = models.CharField(verbose_name="Тип мероприятия", max_length=255)

    def __str__(self):
        return self.title


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
    photo = models.ImageField(upload_to='uploads/', default='uploads/default.png')

    def save(self, *args, **kwargs):
        # Calculate and set the initial value of available_seats

        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


