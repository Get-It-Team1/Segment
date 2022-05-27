from django.contrib import admin
from .models import Experience, Review, Tag

# Register your models here.

admin.site.register(Review)
admin.site.register(Experience)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug':('name',) }

admin.site.register(Tag, TagAdmin) 