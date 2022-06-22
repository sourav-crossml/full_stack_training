from random import choices
from secrets import choice
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

pipeline_select_options = (
    (0, 'Engine-I'),
    (1, 'Engine-II'),
)

classification_model_select_options = (
    (0, 'Engine-I'),
    (1, 'Engine-II'),
)

input_document_select_options = (
    (0, 'JPG'),
    (1, 'PDF'),
    (2, 'JPEG'),
    (3, 'TIF'),
    (4, 'PNG'),
)
time_zone_select_options = (
    (0, '(UTC-12:00)Universal Coordinated Time GMT '),
    (1, '(EET) Eastern European Time GMT+2:00'),
    (2, '(IST) India Standard Time	GMT+5:30'),
)

process_sla_select_options = (
    (0, '1 hours'),
    (1, '2 hours'),
    (2, '3 hours'),
    (3, '4 hours'),
    (4, '5 hours'),
    (5, '6 hours'),
    (6, '7 hours'),
    (7, '8 hours'),
    (8, '9 hours'),
    (9, '10 hours'),
    (10, '11 hours'),
    (11, '12 hours'),
    (12, '13 hours'),
    (13, '14 hours'),
    (14, '15 hours'),
    (15, '16 hours'),
    (16, '17 hours'),
    (17, '18 hours'),
    (18, '19 hours'),
    (19, '20 hours'),
    (20, '21 hours'),
    (21, '22 hours'),
    (22, '23 hours'),
    (23, '24 hours'),
)

pre_processing_select_options = (
    (0, 'no'),
    (1, 'yes'),
)
# Create your models here.


class NewProcess(models.Model):
    process_name = models.CharField(max_length=30)
    pipeline = models.CharField(max_length=1, choices=pipeline_select_options)
    classication_model = models.CharField(
        max_length=1, choices=classification_model_select_options)
    input_document = MultiSelectField(
        choices=input_document_select_options)
    time_zone = models.CharField(
        max_length=1, choices=time_zone_select_options)
    process_sla = models.CharField(
        max_length=1, choices=process_sla_select_options)
    pre_processing = models.CharField(
        max_length=1, choices=pre_processing_select_options)
    username= models.ForeignKey(User, to_field="username",on_delete=models.CASCADE)