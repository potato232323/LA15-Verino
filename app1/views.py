from django.shortcuts import render, get_object_or_404
from .models import Post

def say_hello(request):
    return HttpResponse('Hello Django')

def say_hi(request):
    return render(request, 'hi.html', {'name': 'Allyson Verino'})

def blog_list(request):
    posts = Post.objects.all()  
    context = {
        'blog_list': posts  
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, id):
    each_post = get_object_or_404(Post, id=id)  
    context = {
        'blog_detail': each_post
    }
    return render(request, 'blog_detail.html', context)
