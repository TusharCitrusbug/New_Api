from django.contrib import admin

from .models import CSV_STORE, Category, City, Plan


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_image', 'featured')
    list_filter = ('featured',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'description',
        'plan_datetime',
        'city',
        'postal_code',
        'plan_image',
        'category',
        'is_active',
    )
    list_filter = ('plan_datetime', 'is_active')

@admin.register(CSV_STORE)
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'csv_file',
    )