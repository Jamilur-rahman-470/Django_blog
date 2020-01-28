from django.shortcuts import render
from .models import HeaderText, Posts
from django.views import generic

# Create your views here.
def getHomePage(request):
    data = HeaderText.objects.all()[0]
    posts = Posts.objects.all()
    return render(request, 'pages/index.html', {'banner': data, 'posts': posts})

def getBlogPage(request):
    posts = Posts.objects.all()
    return render(request, 'pages/blog.html', {'posts': posts})

def getAboutPage(request):
    return render(request, 'pages/about.html')

def getContactPage(request):
    return render(request, 'pages/contact.html')

class PostList(generic.ListView):
    queryset = Posts.objects.all()
    template_name = 'pages/index.html'

class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'pages/post_detail.html'
