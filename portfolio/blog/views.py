from django.shortcuts import render
from .models import post, comment, category
from .forms import comment_form
from django.http import HttpResponseRedirect
# def preview(request):
#     return render(request, 'preview.html')
def blog_index(request):
    all_posts=post.objects.all()
    context={
        'all_posts':all_posts
    }
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk): #первичный ключ конкретного поста
    one_post=post.objects.get(pk=pk)
    comments=comment.objects.filter(post=one_post)
    form=comment_form()
    if request.method=='POST':
        form=comment_form(request.POST)
        if form.is_valid():
            my_comment=comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=one_post)
            my_comment.save()
            return HttpResponseRedirect(f'/blog/{pk}')
    context={
        'one_post':one_post,
        'comments':comments,
        'form':form}
    return render(request, 'blog_detail.html', context)

def blog_category(request,category):
    all_posts=post.objects.filter(categ__name__contains=category).order_by('created_on')
    context={'category':category, 'posts':all_posts}
    return render(request, 'blog_category.html', context)
