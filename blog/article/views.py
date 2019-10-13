from django.shortcuts import render , redirect , HttpResponse
from .models import ArticlePost
import markdown
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Article_List(request):
    articles = ArticlePost.objects.all()
    context = {'articles':articles}
    return render(request,'article/list.html',context)

def Article_detail(request,id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                     ])
    context = {'article':article}
    return render(request,'article/detail.html',context)

@login_required(login_url='control/login')
def Article_create(request):
    if request.method =='POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect('Article_List')
        else:
            return HttpResponse('表单内容有误，请重新填写')
    else:
        article_post_form = ArticlePostForm()
        context = {'article_pst_form':article_post_form}
        return render(request,'article/create.html',context)

def Article_delete(request,id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('Article_List')

def Article_safe_delete(request,id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect('Article_List')
    else:
        return HttpResponse('仅允许POST请求')

def Article_update(request,id):
    article = ArticlePost.objects.get(id=id)

    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('Article_detail',id=id)
        else:
            HttpResponse('表单内容有误，请重新填写。')
    else:

        article_post_form = ArticlePostForm()
        context = {'article':article,'article_post_form':article_post_form}
        return render(request,'article/update.html',context)