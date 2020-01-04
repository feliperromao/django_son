from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Olá mundo!')


def home_with_param(request, post_id):
    return HttpResponse(f'Voce solicitou o posst {post_id}')


def post_list(request):
    data = {
        'name': 'Felipe Romão',
        'email': 'feliperomaocad@gmail.com'
    }
    return render(request, 'posts_list.html', data)