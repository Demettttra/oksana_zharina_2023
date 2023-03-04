from django.shortcuts import render
from .models import project

def project_index(request):
    all_posts=project.objects.all()
    context={
        'all_posts':all_posts
    }
    return render(request, 'project_index.html', context)
def project_detail(request, pk):
    one_post=project.objects.get(pk=pk)
    context={
        'one_post':one_post
    }
    return render(request, 'project_detail.html', context)
