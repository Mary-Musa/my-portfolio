from django.shortcuts import render
from projects.models import project  # Keeping your class name as 'project'
from django.http import Http404

# Create your views here.
# projects/views.py

def project_index(request):
    projects = project.objects.all()  # Use the lowercase class name here
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    try:
        # Try to get the project by its primary key
        single_project = project.objects.get(pk=pk)  # Use the lowercase class name here
    except project.DoesNotExist:
        # If project is not found, raise a 404 error
        raise Http404("Project does not exist")
    
    context = {
        "project": single_project  # Updated variable name to avoid conflict
    }
    # Render the template with the specific project's details
    return render(request, "projects/project_detail.html", context)
