from django.contrib import admin
from django.utils.html import format_html
from .models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
  
  def thumbnail(self, object):
    return format_html('<img src="{}" width="30" style="border-radius: 50px;" />'.format(object.car_photo.url))

  thumbnail.short_description = 'Car Image'

  list_display = ('id', 'thumbnail', 'brand', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
  list_display_links = ('id', 'thumbnail', 'brand', 'car_title',)
  list_editable = ('is_featured',)
  search_fields = ('brand', 'car_title', 'city', 'model', 'condition', 'body_style')
  list_filter = ('brand', 'condition', 'body_style')



admin.site.register(Car, CarAdmin)