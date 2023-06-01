from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages # 오류발생 창을 위한 messages

# Create your views here.
def index(request):
    return render(request, 'mainapp/lobby.html')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id) # Question.objects.get의 상위호환이다. 실패하면 404오류를 전달
    context = {'post': post}
    return render(request, 'mainapp/detail.html', context) # question_detail.html에 있는 question에 context를 전달

@login_required(login_url='user:login')
def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.voter.add(request.user) # 추천인 속성에 유저를 추가
    return redirect('main:detail', post_id=post.id)

@login_required(login_url='user:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('main:detail', post_id=post.id)
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'mainapp/detail.html', context)

@login_required(login_url='user:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('main:detail', post_id=comment.post.id)  
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment) # 새로운 내용으로 폼 업데이트후
        if form.is_valid():
            comment = form.save(commit=False) # 폼저장 (수정완료)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('main:detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'mainapp/detail_modify.html', context)

@login_required(login_url='user:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('main:detail', post_id=comment.post.id)

def list1(request):
    post_list = Post.objects.filter(category=1) # Post 중 카테고리 1 (한식)만 반환
    context = {'post_list': post_list}
    return render(request, 'mainapp/list1.html', context)

def list2(request):
    post_list = Post.objects.filter(category=2) # Post 중 카테고리 2 (일식)만 반환
    context = {'post_list': post_list}
    return render(request, 'mainapp/list2.html', context)

def list3(request):
    post_list = Post.objects.filter(category=3) # Post 중 카테고리 3 (중식)만 반환
    context = {'post_list': post_list}
    return render(request, 'mainapp/list3.html', context)

def list4(request):
    return render(request, 'mainapp/list4.html')
