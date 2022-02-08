from django.shortcuts import render
from .models import Blog


def all_articles(request):
    """ Render all articles """

    blogs = Blog.objects.all().order_by('-created_on')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)
