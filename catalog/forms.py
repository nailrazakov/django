from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        unacceptable_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                              'радар',)
        if cleaned_name in unacceptable_words:
            raise forms.ValidationError('Данное наименование не допустимо')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        unacceptable_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                              'радар', ]
        if cleaned_description in unacceptable_words:
            raise forms.ValidationError('Данное описание не допустимо')
        return cleaned_description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                field.widget.attrs['class'] = 'form-check-input'
            field.widget.attrs['class'] = 'form-control'
