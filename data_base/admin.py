from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class NameCategiriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class RazAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class GlavAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("theme",)}
    list_display = Theme.displayFields
    search_fields = Theme.searchFields
    list_filter = Theme.filterFields

class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("fio",)}

class ComputerAdmin(admin.ModelAdmin):
    list_filter = Computers.filterFields
    search_fields = ['name', 'invb', 'invm', 'id_kabinet__name']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(NameCategories, CategoriesAdmin)
admin.site.register(Raz, RazAdmin)
admin.site.register(Glav, GlavAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(News)
admin.site.register(About, AboutAdmin)
admin.site.register(Program)
admin.site.register(Laborant)
admin.site.register(Kabinet)
admin.site.register(Computers, ComputerAdmin)
