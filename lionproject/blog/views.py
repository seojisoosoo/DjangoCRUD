from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

def home(request):
    blogs=Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog=get_object_or_404(Blog, pk=id)
    # 객체를 갖고 오거나 못 찾으면 404띄워라
    # primary key
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog =Blog()
    new_blog.title=request.POST['title']
    new_blog.writer=request.POST['writer']
    new_blog.body=request.POST['body']
    new_blog.pub_date=timezone.now()
    # 현재 시간알려주는 모듈
    new_blog.save()

    # 정보는 위와같이 작성해서 받아온다
    # ['']이 안에 들어가는 변수들은 new.html의 name들
    return redirect('detail', new_blog.id)
    # 요청이 보내졌을 때, return되는 것. 
    # 뭘 만들어서 어디 보내는 게 아니라 원래 있던 페이지로 돌아가야하므로, render가 아닌 redirect이용

def edit(request, id):
    edit_blog=Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST['title']
    update_blog.writer=request.POST['writer']
    update_blog.body=request.POST['body']
    update_blog.pub_date=timezone.now()
    # 현재 시간알려주는 모듈
    update_blog.save()

    return redirect('detail', update_blog.id)
