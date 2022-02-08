from django.shortcuts import render

from blogs.models import Blog


def index(request):
    """ Home Page """
    
    blogs = Blog.objects.all().order_by('-created_on')[0:3]
    context = {
        'blogs': blogs,
    }

    return render(request, 'home/index.html', context)