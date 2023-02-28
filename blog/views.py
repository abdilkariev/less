from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': '0 клубе Python bytes'})

posts = [
{
    'author': 'Администратор',
    'title': 'Our first post',
    'content': 'content of our post',
    'date_posted': '12 may, 2023',
},
{
    'author': 'Администратор',
    'title': 'Our first post',
    'content': 'content of our post',
    'date_posted': '12 may, 2023',  
}
]