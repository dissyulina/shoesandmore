from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Model to Add / Edit Review
    """
    class Meta:
        model = Review
        fields = ('rating', 'review_text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
