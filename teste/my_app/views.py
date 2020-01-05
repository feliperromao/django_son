from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category

# Create your views here.

def home(request):
    # return HttpResponse('Olá mundo!')
    return render(request, 'index.html')


def home_with_param(request, post_id):
    return HttpResponse(f'Voce solicitou o posst {post_id}')


def post_list(request):

    if 'category_id' in request.GET:
        category_id = request.GET['category_id']
        category = Category.objects.get(id=category_id)
        posts = Post.objects.filter(categories=category)
    else:
        posts = Post.objects.all()

    categories = Category.objects.all()
    data = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'posts_list.html', data)


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    data = {
        'post': post,
        'categories': categories
    }
    return render(request, 'post_show.html', data)