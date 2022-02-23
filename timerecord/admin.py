from django.contrib import admin
from .models import Goal, Category

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):

#     list_filter = ('title', 'description', 'color', 'goal')

# Inlines
class CategoryInline(admin.StackedInline):
    model = Category
    fields = ('title', 'description', 'color')
    max_num = 4


class GoalAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

admin.site.register(Goal, GoalAdmin)
# admin.site.register(Category, CategoryInline)