from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Model to Add / Edit Review
    """
    class Meta:
        model = Review
        exclude = ('rating', 'review')


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, set autofocus on review field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'reviews': 'Write your review here',
        }

        self.fields['review'].widget.attrs['autofocus'] = True

