from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    return HttpResponse('Olá mundo!')


def home_with_param(request, post_id):
    return HttpResponse(f'Voce solicitou o posst {post_id}')


def post_list(request):
    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'posts_list.html', data)


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_show.html', {'post':post})