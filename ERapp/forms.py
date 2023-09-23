from django import forms
from .models import TableData1

class TableDataForm1(forms.ModelForm):
    class Meta:
        model = TableData1
        fields = ['cell_data']