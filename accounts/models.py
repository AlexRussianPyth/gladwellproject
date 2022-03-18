from django.db import models
from django.contrib.auth.models import User

class Achiever(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Фото пользователя", null=True, blank=True)
    about = models.TextField(blank=True)
# TODO Здесь должен быть только один инстанс на Юзера! Ограничить создание второго и написать тест

