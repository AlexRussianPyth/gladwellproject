from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Goal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название цели", null=False, blank=False)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(verbose_name="Описание цели")
    target_hours = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)], verbose_name="Часов необходимо")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name="Значимость")
    created_at = models.DateTimeField(auto_now_add=True)
    is_achieved = models.BooleanField(default=False, verbose_name="Achieved?")
    image = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name="Изображение цели", null=True)

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