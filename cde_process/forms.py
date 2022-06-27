from dataclasses import fields
from django import forms
from .models import NewProcess,AddCnn


# Create your forms here.
class NewProcessForm(forms.ModelForm):

    class Meta:
        model = NewProcess
        fields = '__all__'
        # fields = ('process_name', 'pipeline', 'classification_model', 'input_document', 'time_zone','process_sla','pre_processing')
class AddCnnForm(forms.ModelForm):

    class Meta:
        model = AddCnn
        exclude = ["sample_file"]
        # fields = ('process_name', 'pipeline', 'classification_model', 'input_document', 'time_zone','process_sla','pre_processing')