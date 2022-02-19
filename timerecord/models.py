from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Goal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название цели", null=False, blank=False)
    slug = models.SlugField(unique=True)
    # MAKE TEST check slugify
    description = models.TextField()
    target_hours = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_achieved = models.BooleanField(default=False)
    image = models.ImageField(verbose_name="Изображение цели")

    def get_absolute_url(self):
        pass

    def __str__(self):
        return f"Goal: {self.name}, comment: {self.description[:20]}, rating: {self.rating}"
