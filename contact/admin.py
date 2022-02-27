from django.contrib import admin
from .models import Topic, Contact


class TopicAdmin(admin.ModelAdmin):
    """ Topic for Contact Form"""

    list_display = (
        'subject',
        'text',
    )


class ContactAdmin(admin.ModelAdmin):
    """ Contact Table """

    list_display = (
        'name',
        'email',
        'order_number',
        'topic',
        'message',
        'date'
    )
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


admin.site.register(Topic, TopicAdmin)
admin.site.register(Contact, ContactAdmin)
