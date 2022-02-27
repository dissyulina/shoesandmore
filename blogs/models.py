from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """ Blog Model """

    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    title = models.CharField(max_length=254)
    paragraph1 = models.TextField(null=False, blank=False)
    paragraph2 = models.TextField(null=True, blank=True)
    paragraph3 = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
