from django.shortcuts import render
from .models import Post
from datetime import date

def posts(request):
    posts = Post.objects.filter(pub_date__lte=date.today())
    cssclass = 'apost'
    title = 'The Blog | Jersey City | Arts on the Hudson'
    variables = {'posts':posts, 'title':title, 'cssclass':cssclass}
    return render(request,'blog/blog.html',variables)

def post(request,id):
    post = Post.objects.get(pk = id, pub_date__lte=date.today() )
    cssclass = 'apost'
    title = post.headline + ' | Jersey City | Arts on the Hudson'
    variables = {'post':post, 'title':title, 'cssclass':cssclass}
    return render(request,'blog/post.html',variables)

# Create your views here.