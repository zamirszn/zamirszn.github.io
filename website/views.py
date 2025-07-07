from django.shortcuts import get_object_or_404, render
from collections import defaultdict
from django.utils import timezone

from website.models import Project

from collections import OrderedDict

def portfolio(request):
    projects = Project.objects.prefetch_related('images').order_by('-year')
    
    # Get distinct years from projects
    project_years = sorted(projects.values_list('year', flat=True).distinct(), reverse=True)
    
    # Get selected year from query
    selected_year = request.GET.get('year')
    try:
        selected_year = int(selected_year)
    except (ValueError, TypeError):
        selected_year = project_years[0] if project_years else timezone.now().year
    
    # Build a dictionary: year -> 1 project (featured preferred)
    year_projects = OrderedDict()
    for year in project_years:
        year_projects[year] = (
            projects.filter(year=year, featured=True).first()
            or projects.filter(year=year).first()
        )
    
    # Project to show in slider
    current_project = year_projects.get(selected_year)
    
    # Add total projects count
    total_projects = projects.count()
    
    # For the projects template section
    featured = projects.filter(featured=True).first()  # Get the main featured project
    other_projects = projects.exclude(id=featured.id if featured else None)[:4]  # Get other projects (limit to 4)
    
    context = {
        'project_years': project_years,
        'selected_year': selected_year,
        'year_projects': year_projects,
        'current_project': current_project,
        'total_projects': total_projects,
        'featured': featured,  # For the main featured section
        'projects': other_projects,  # For the projects list
    }
    
    return render(request, 'website/portfolio.html', context)

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'website/project_detail.html', {'project': project})