from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    cover_image = models.ImageField(upload_to='projects/covers/')
    preview_link = models.URLField(blank=True)
    case_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    year = models.PositiveIntegerField(
         default=timezone.now().year,
        help_text="Year the project was completed",
        validators=[MinValueValidator(2000), MaxValueValidator(timezone.now().year + 1)]
    )

    def __str__(self):
        return f"{self.title} ({self.year})"

   

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"
