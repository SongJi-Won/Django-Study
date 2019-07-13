from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.GET['title']
    new_blog.pub_date = timezone.datetime.now()
    new_blog.body = request.GET['body']
    new_blog.save()
    return redirect('/blog/'+str(new_blog.id))