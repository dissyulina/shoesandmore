from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin settings to display list of Reviews
    """

    model = Review
    list_display = (
        'product',
        'date',
        'user',
        'rating',
        'review_text',
    )

    ordering = ('-product', '-date')
    list_filter = ('rating',)


admin.site.register(Review, ReviewAdmin)
