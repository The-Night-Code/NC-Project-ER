from django import forms
from .models import TableData1, ImageModel 

class TableDataForm1(forms.ModelForm):
    class Meta:
        model = TableData1
        fields = ['cell_data']
        
        
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['imageTitle', 'image']
        
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        
        model = ImageModel
        fields = ('imageTitle', 'image')