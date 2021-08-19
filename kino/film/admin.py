from django.contrib import admin

from .models import Film


class FilmAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields': ['about']}),
        ('Date information', {'fields': ['add_date']}),
    ]


admin.site.register(Film, FilmAdmin)
