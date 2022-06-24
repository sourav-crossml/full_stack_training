from django import forms
from .models import NewProcess 


# Create your forms here.
class NewProcessForm(forms.ModelForm):

    class Meta:
        model = NewProcess
        fields = ('process_name', 'pipeline', 'classification_model', 'input_document', 'time_zone','process_sla','pre_processing')
        