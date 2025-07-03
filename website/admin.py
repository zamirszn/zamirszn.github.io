from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    save_as = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'featured')
    list_filter = ('featured', 'category')
    search_fields = ('title', 'description')
    inlines = [ProjectImageInline]
