from audioop import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from pip._vendor.requests import Response
from django.core.exceptions import ObjectDoesNotExist

#여기서 게시물 list 가져오는 부분 빼고 class로 묶고, 저번에 아려준 apiview로 post, get, put, del 메소드 받아서 어떤 작업 수행할껀지 구별하고
#함수로 뿌려주는 형식..?
#수정하게 되면 사실상 다 수정해야해서 거의 다른작업하는 느낌날텐데......................................................
#경험으로는 무조건 좋은 경험이긴한데..
# Create your views here.
def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)


def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'post.html')


def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})


@csrf_exempt
def edit(request, id):
    board = Board.objects.filter(pk=id)

    return render(request, "edit.html", {'board': board})

#살려주세요...
#토나와요....
#ㅠㅠㅠㅠㅠ
#자고싶어요.....

@csrf_exempt
def update(request, id):

    update_author = request.GET['author']
    update_title = request.GET['title']
    update_content = request.GET['content']

    try:
        board = Board.objects.get(pk=id)
        if update_author != "":
            #board.author = update_title 오타 실화 ㅎ
            board.author = update_author
        if update_title != "":
            board.title = update_title
        if update_content != "":
            board.content = update_content

        try:
            board.save()
            return redirect('index')
        except ValueError:
            return Response({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return Response({"success": False, "msg": "게시글 없음"})


@csrf_exempt
def delete(request, id):
    board_delete = Board.objects.get(pk=id)
    board_delete.delete()

    return redirect('index')


