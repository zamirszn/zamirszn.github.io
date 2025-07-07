from django.contrib import admin
from .models import Project, ProjectImage
from unfold.admin import ModelAdmin, TabularInline
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


class ProjectImageInline(TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    export_form_class = SelectableFieldsExportForm
    save_as = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'featured', "year")
    list_filter = ('featured', 'category' , "year")
    search_fields = ('title', 'description' , "year")
    inlines = [ProjectImageInline]
