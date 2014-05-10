from django.shortcuts import render

from projects.models import Projects
from members.forms import LoginForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    projects = Projects.objects.order_by('-date_of_publication')[:6]
    form = LoginForm()
    return render(request, 'projects/home.html', {'projects': projects, 'form':form})
    
def index(request):
    projects_list = Psrojects.objects.order_by('-date_of_publication')
    paginator = Paginator(projects, 10)
    
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    
    return render(request, 'projects/index.html', {'projects': projects})
