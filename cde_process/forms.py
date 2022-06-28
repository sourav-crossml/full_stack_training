from dataclasses import fields
from django import forms
from .models import NewProcess,AddCnn


# Create your forms here.
class NewProcessForm(forms.ModelForm):

    class Meta:
        model = NewProcess
        fields = '__all__'
 
class AddCnnForm(forms.ModelForm):

    class Meta:
        model = AddCnn
        exclude = ["sample_file"]

class ManageAttributeForm(forms.ModelForm):

    class Meta:
        model = AddCnn
        exclude = ["data_label"]
       