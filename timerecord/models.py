from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class GoalQuerySet(models.QuerySet):
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

    def my_function_field(self):
        if self.target_hours <= 15:
            return "Small Goal"
        else:
            return "Long Goal"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('timerecord:goal-detail', kwargs={'slug':self.slug})

    def __str__(self):
        return f"Goal: {self.name} with rating: {self.rating}"

class Category(models.Model):
    RGB_COLORS_FOR_CATEGORY = [
        ('Blue', '66, 135, 245'),
        ('Red', '181, 0, 36'),
        ('Green', '0, 143, 12'),
        ('Orange', '194, 101, 2')
    ]

    title = models.CharField(max_length=30, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание категории")
    color = models.CharField(max_length=10, choices=RGB_COLORS_FOR_CATEGORY, default="Red")
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.title} category for {self.goal.name}"
    
    def get_absolute_url(self):
        pass


class TimeRecord(models.Model):
    time_added = models.IntegerField(verbose_name="Времени добавлено", validators=[MinValueValidator(1)])
    date = models.DateField(verbose_name="Дата активности", auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)