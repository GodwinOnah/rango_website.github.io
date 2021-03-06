from django.contrib import admin
from rango.models import Category, Page


admin.site.register(Page)
admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'category', 'url')
