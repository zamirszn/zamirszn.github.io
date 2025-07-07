# views.py
from django.shortcuts import render
from collections import OrderedDict
from django.utils import timezone
from website.models import Project
import random

def portfolio(request):
    projects = Project.objects.prefetch_related('images').order_by('-year')

    project_years = sorted(projects.values_list('year', flat=True).distinct(), reverse=True)

    selected_year = request.GET.get('year')
    try:
        selected_year = int(selected_year)
    except (ValueError, TypeError):
        selected_year = project_years[0] if project_years else timezone.now().year

    year_projects = OrderedDict()
    for year in project_years:
        year_projects[year] = (
            projects.filter(year=year, featured=True).first()
            or projects.filter(year=year).first()
        )

    current_project = year_projects.get(selected_year)

    total_projects = projects.count()

    featured = projects.filter(featured=True).first()
    other_projects = projects.exclude(id=featured.id if featured else None)[:4]

    slider_projects = list(projects.exclude(cover_image='').order_by('?')[:3])

    context = {
        'project_years': project_years,
        'selected_year': selected_year,
        'year_projects': year_projects,
        'current_project': current_project,
        'total_projects': total_projects,
        'featured': featured,
        'projects': other_projects,
        'slider_projects': slider_projects,
    }

    return render(request, 'website/portfolio.html', context)
