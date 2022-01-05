from django.contrib import admin
from .models import PoliticianDetail
from django.utils.html import format_html

# Register your models here.
class PoliticianDetailAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img scr="{}" width = "20px"/>'.format(object.photo.url))

    list_display = ('id', 'myphoto','first_name', 'last_name')
    list_display_links = ('first_name','last_name',)
    search_fields = ('first_name',)
    
admin.site.register(PoliticianDetail, PoliticianDetailAdmin)

