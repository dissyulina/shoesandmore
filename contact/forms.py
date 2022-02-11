from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Topic, Contact


class ContactForm(forms.ModelForm):
    """ Contact Form """

    class Meta:
        """ Specify model, fields, and label """
        model = Contact
        fields = ('name', 'email', 'order_number',
                  'topic', 'message')
        labels = {
            'name': _('Full Name'),
            'email': _('Email Address'),
            'order_number': _('Order Number'),
            'topic': _('Topic (Choose One)'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        topic = Topic.objects.all()
        topic_text = [(t.id, t.get_text()) for t in topic]

        self.fields['topic'].choices = topic_text
