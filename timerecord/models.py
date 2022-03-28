from django.db import models
from colorfield.fields import ColorField
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class GoalQuerySet(models.QuerySet):
    """Allow to search Goal Model by 2 fields simultaneously - by 'name' and 'description' """
    def search(self, query=None):
        if query is None or query == "":
            return self.get_queryset().none()
        
        lookups = Q(name__icontains=query) | Q(description__icontains=query)
        return self.filter(lookups)

class GoalManager(models.Manager):

    def get_queryset(self):
        return GoalQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Goal(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, verbose_name="Название цели", null=False, blank=False, unique=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(verbose_name="Описание цели")
    target_hours = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)], verbose_name="Часов необходимо")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name="Значимость")
    created_at = models.DateTimeField(auto_now_add=True)
    is_achieved = models.BooleanField(default=False, verbose_name="Achieved?")
    image = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение цели", null=True, blank=True)

    objects = GoalManager()

    # TODO Для более быстрой работы нам нужно создать сводную таблицу, которая будет обновляться только при 
    # добавлении объекта TimeRecord. Тогда нам не придется каждый раз дергать базу.
    def check_progress(self):
        """Check all categories and timerecords, and return number of hours"""
        category_set = self.category_set.all()

        time_summary = 0

        for category in category_set:
            timerecords = category.timerecord_set.all()
            for timerecord in timerecords:
                time_summary += timerecord.time_added

        return time_summary // 60

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('timerecord:goal-detail', kwargs={'slug':self.slug})

    def __str__(self):
        return f"Goal: {self.name} with rating: {self.rating}"

class Category(models.Model):
    """
    We use this model for assigning a category (part of the goal).
    Samples (color_palette) don't restrict user, just add some useful colors.
    """

    COLOR_PALETTE = [
        ('#FFFFFF', 'white', ),
        ('#000000', 'black', ),
    ]

    title = models.CharField(max_length=30, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание категории")
    color = ColorField(format='hex', default='#006CFF', samples=COLOR_PALETTE)
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.title} category for {self.goal.name}"
    
    def get_absolute_url(self):
        return self.goal.get_absolute_url()
    
    def get_timerecords(self):
        return self.timerecord_set.all()

    def add_timerecord(self, minutes):
        TimeRecord(category=self, time_added=minutes).save()
        return None

class TimeRecord(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    time_added = models.IntegerField(verbose_name="Времени добавлено", validators=[MinValueValidator(1)])
    date = models.DateField(verbose_name="Дата активности", auto_now_add=True)

    def __str__(self):
        return f"Время для:{self.category} добавлено {self.time_added} {self.date}"