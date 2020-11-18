from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .models import Article,Comment
from .forms import AddartilceForm
# Create your views here.

from django.contrib import messages

def index(request):
    context={
        "ad":"TAYFUN",
        "soyad":"KAYA",
        "bilgiler":["Fenerbahçeli","Birisi..."]
    }
    return render(request,"index.html",context)

def hakkımızda(request):
    return render(request,"hakkımızda.html")

# Makale gösterme sayfası

def articles(request):

    keyword=request.GET.get("keyword")
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

# **********

@login_required(login_url="user:login")
def dashboard(request):

    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)


@login_required(login_url="user:login")
def addarticle(request):
    form=AddartilceForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale Başarıyla eklendi")
        return redirect("article:dashboard")
    context={
        "form":form
    }
    return render(request,"addarticle.html",context)


@login_required(login_url="user:login")
def detail(request,id):
    #article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)

    comments=article.comments.all()


    return render(request,"detail.html",{"article":article,"comments":comments})


@login_required(login_url="user:login")
def update(request,id):
    article=get_object_or_404(Article,id=id)

    form=AddartilceForm(request.POST or None,request.FILES or None,instance=article )

    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale Başarıyla güncellendi")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})


@login_required(login_url="user:login")
def delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("article:dashboard")


@login_required(login_url="user:login")
def comment(request,id):
    article=get_object_or_404(Article,id=id)

    if request.method=="POST":
        comment_author=request.POST.get("comment-author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))