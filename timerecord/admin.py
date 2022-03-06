from django.contrib import admin
from .models import Goal, Category

# class CategoryAdmin(admin.ModelAdmin):

#     list_filter = ('title', 'description', 'color', 'goal')

# Inlines
class CategoryInline(admin.StackedInline):
    model = Category
    fields = ('title', 'description', 'color')

    def get_extra(self, request, obj=None, **kwargs):
        return 1


class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'target_hours']
    list_display_links = ['name']
    search_fields = ['name']
    inlines = [CategoryInline]

admin.site.register(Goal, GoalAdmin)
# admin.site.register(Category, CategoryInline)