from django.contrib import admin
from .models import Project, ProjectImage
from unfold.admin import ModelAdmin, TabularInline


class ProjectImageInline(TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    save_as = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'featured', "year")
    list_filter = ('featured', 'category' , "year")
    search_fields = ('title', 'description' , "year")
    inlines = [ProjectImageInline]
