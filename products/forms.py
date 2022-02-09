from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Product Form to add/ update products """

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names_cat = [(c.id, c.get_friendly_name()) for c in categories]
        
        subcategories = Subcategory.objects.all()
        friendly_names_sub = [(s.id, s.get_friendly_name()) for s in subcategories]

        self.fields['category'].choices = friendly_names_cat
        self.fields['subcategory'].choices = friendly_names_sub
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
