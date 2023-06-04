from django.contrib.auth.models import AbstractUser
from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=64, blank=False)
    phone = models.CharField(max_length=64, blank=False)
    date = models.CharField(max_length=15)

    def __str__(self):
        return 'Заявка от: ' + self.name

class Feedback(models.Model):
    name = models.CharField(max_length=64, blank=False)
    mail = models.EmailField(max_length=128, blank=False)
    message = models.CharField(max_length=256, blank=False)
    date = models.CharField(max_length=15)

    def __str__(self):
        return 'Обратная связь от: ' + self.name

class User(AbstractUser):
    name = models.CharField(verbose_name='Имя', max_length=64, blank=False)
    phone = models.CharField(verbose_name='Телефон', max_length=64, blank=False)
    mail = models.CharField(verbose_name='Email', max_length=128, blank=False, unique=True)
    username = models.CharField(verbose_name='Имя пользователя', max_length=64, blank=True)
    password = models.CharField(verbose_name='Пароль', max_length=128, blank=False)

    USERNAME_FIELD = 'mail'

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя', blank=False)
    message = models.TextField(max_length=128, verbose_name='Отзыв', blank=False)
    date = models.CharField(max_length=11, verbose_name='Дата отправки', blank=True)

    def __str__(self):
        return 'Комментарий от ' + self.name + ', Дата: ' + self.date