from django import forms
from .models import Gallery


class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image']
        # exclude = ['rating']
        # fields = '__all__'

        labels = {
            'image': 'Изображение'
        }
