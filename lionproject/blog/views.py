from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.http import JsonResponse
import json

# def home(request):
#     blogs=Blog.objects.all()
#     return render(request, 'home.html', {'blogs':blogs})


def home(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        blog_list = []
        for blog in blogs:
            blog_list.append({'title': blog.title,
                              'writer': blog.writer,
                              'body': blog.body, })

        return JsonResponse({
            'data': blog_list
        })
    elif request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))

        blog = Blog.objects.create(
            title=body['title'],
            writer=body['writer'],
            body=body['body'],
            pub_date=timezone.now()
        )
        return JsonResponse({
            'ok': True,
            'data': {'title': blog.title,
                     'writer': blog.writer,
                     'body': blog.body, }
        })
    # elif request.method == 'PUT':
    #     body = json.loads(request.body.decode('utf-8'))
    #     update = get_object_or_404(Blog, pk=id)
    #     update.title = body['title'],
    #     update.writer = body['writer'],
    #     update.body = body['body'],
    #     update.pub_date = timezone.now()
    #     update.save()
    #     return JsonResponse({
    #         'data': {'title': update.title,
    #                  'writer': update.writer,
    #                  'body': update.body, }
    #     })
    # elif request.method == 'DELETE':
    #     delete = get_object_or_404(Blog, pk=id)
    #     delete.delete()
    #     return JsonResponse({
    #         'data': None
    #     })

        # 정보는 위와같이 작성해서 받아온다
        # ['']이 안에 들어가는 변수들은 new.html의 name들
        # return redirect('detail', new_blog.id)
        # 요청이 보내졌을 때, return되는 것.
        # 뭘 만들어서 어디 보내는 게 아니라 원래 있던 페이지로 돌아가야하므로, render가 아닌 redirect이용


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    # 객체를 갖고 오거나 못 찾으면 404띄워라
    # primary key
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    return render(request, 'new.html')


# def create(request):


def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})


def update(request, id):
    # update_blog = Blog.objects.get(id=id)
    # update_blog.title = request.POST['title']
    # update_blog.writer = request.POST['writer']
    # update_blog.body = request.POST['body']
    # update_blog.pub_date = timezone.now()
    # # 현재 시간알려주는 모듈
    # update_blog.save()

    # return redirect('detail', update_blog.id)
    if request.method == "PUT":
        # 변경내용이 들어가 있는 body 수신
        body = json.loads(request.body.decode('utf-8'))

        # 변강할 category 가져와서 해당 변수에 저장
        update_blog = get_object_or_404(Blog, pk=id)

        # 변수.필드명 을 통해 해당 속성에 접근, 변경(생셩과 비슷)
        update_blog.title = body['title']
        update_blog.writer = body['writer']
        update_blog.body = body['body']

        # 해당과정으로 변경할 경우 꼭 .save()를 통해 저장 필요
        update_blog.save()

        return JsonResponse({
            'data': update_blog
        })


def delete(request, id):
    # delete_blog = Blog.objects.get(id=id)
    # delete_blog.delete()
    # # 위에서는 save를 했다면, 여기서는 delete
    # return redirect('home')
    if request.method == "DELETE":
        delete_category = get_object_or_404(Blog, pk=id)
        # 그냥 이렇게 삭제하면 됨,,ㅎ
        delete_category.delete()
        return JsonResponse({
            'data': None  # 삭제의 경우 성공해도 데이터를 줄게 없음
        })
