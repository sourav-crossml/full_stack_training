from django.db import models

pipeline_select_options = (
    (0,'Engine-I'),
    (1,'Engine-II')
)

classification_model_select_options = (
    (0,'Engine-I'),
    (1,'Engine-II')
)

# Create your models here.
class NewProcess(models.Model):
    process_name = models.CharField(max_length=30)
    pipeline = models.CharField(max_length=1,choices=pipeline_select_options)
    classication_model = models.CharField(max_length=1,choices=classification_model_select_options)

    