from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs=Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog=get_object_or_404(Blog, pk=id)
    # 객체를 갖고 오거나 못 찾으면 404띄워라
    # primary key
    return render(request, 'detail.html', {'blog':blog})