from django import forms
from .widgets import CustomClearableFileInput
from django.utils.translation import gettext_lazy as _
from .models import Product, Category, Subcategory


class ProductForm(forms.ModelForm):
    """ Product Form to add/ update products """

    class Meta:
        """ Specify model, fields, and label """
        model = Product
        fields = ('category', 'subcategory', 'sku',
                  'name', 'has_sizes', 'price',
                  'rating', 'image')
        labels = {
            'sku': _('SKU'),
            'has_sizes': _('Has Sizes?'),
        }
        help_texts = {
            'has_sizes': _('Choose YES for shoes and NO for accessories'),
            'rating': _(
                'Please input rating from the manufacturer. The default is 3.'
            ),
        }

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names_cat = [
            (c.id, c.get_friendly_name()) for c in categories
        ]

        subcategories = Subcategory.objects.all()
        friendly_names_sub = [
            (s.id, s.get_friendly_name()) for s in subcategories
        ]

        self.fields['category'].choices = friendly_names_cat
        self.fields['subcategory'].choices = friendly_names_sub
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
