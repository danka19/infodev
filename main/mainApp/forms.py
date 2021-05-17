from django import forms
from django.core.exceptions import ValidationError

from .models import Device, Category


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'category', 'address', 'latitude', 'longitude', 'radius', 'slug']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'latitude': forms.TextInput(attrs={'class': 'form-control'}),
        'longitude': forms.TextInput(attrs={'class': 'form-control'}),
        'radius': forms.TextInput(attrs={'class': 'form-control'}),
        'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not create')
        return new_slug



