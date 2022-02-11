from django.db import models


class Topic(models.Model):
    """ Topic Options for Contact Form """

    subject = models.CharField(max_length=254, null=True, blank=True)
    text = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.subject

    def get_text(self):
        return self.text


class Contact(models.Model):
    """ Contact Model for Contact Form """

    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    topic = models.ForeignKey('Topic', null=True, blank=True, on_delete=models.SET_NULL)
    message = models.TextField(max_length=500, null=False, blank=False)
    order_number = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "-" +  self.email