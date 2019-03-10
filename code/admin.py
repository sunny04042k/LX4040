from django.contrib import admin
from .models import HTML, CSS, JS
# Register your models here.
class POST_CODE(admin.ModelAdmin):
    list_display = ['title','author']
    list_filter = ['author','date']
    search_fields = ['title','author']
admin.site.register(HTML,POST_CODE)
admin.site.register(CSS,POST_CODE)
admin.site.register(JS,POST_CODE)
