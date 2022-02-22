from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin settings to display list of User Profile
    """

    model = UserProfile
    list_display = (
        'user',
        'default_full_name',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_postcode',
        'default_town_or_city',
        'default_country',
    )


admin.site.register(UserProfile, UserProfileAdmin)
