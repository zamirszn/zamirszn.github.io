from django.shortcuts import get_object_or_404, render

from website.models import Project

def portfolio(request):
    featured = Project.objects.filter(featured=True).first()
    others = Project.objects.exclude(id=featured.id) if featured else Project.objects.all()
    return render(request, 'website/portfolio.html', {
        'featured': featured,
        'projects': others,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'website/project_detail.html', {'project': project})