from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    unused_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image', 'purchase_price']

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        for word in self.unused_words:
            if word in cleaned_name:
                raise forms.ValidationError(f'Слово {word} запрещено')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        for word in self.unused_words:
            if word in cleaned_description:
                raise forms.ValidationError(f'Слово {word} запрещено')
        return cleaned_description
