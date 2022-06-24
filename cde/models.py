from pyexpat import model
from random import choices
from secrets import choice
from turtle import mode
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

pipeline_select_options = (
    ('Engine-I', 'Engine-I'),
    ('Engine-II', 'Engine-II'),
)

classification_model_select_options = (
    ('yes', 'yes'),
    ('no', 'no'),
)

input_document_select_options = (
    ('JPG', 'JPG'),
    ('PDF', 'PDF'),
    ('JPEG', 'JPEG'),
    ('TIF', 'TIF'),
    ('PNG', 'PNG'),
)
time_zone_select_options = (
    ('0', '(UTC-12:00)Universal Coordinated Time GMT'),
    ('1', '(EET) Eastern European Time GMT+2:00'),
    ('2', '(IST) India Standard Time	GMT+5:30'),
)

process_sla_select_options = (
    ('0', '1 hours'),
    ('1', '2 hours'),
    ('2', '3 hours'),
    ('3', '4 hours'),
    ('4', '5 hours'),
    ('5', '6 hours'),
    ('6', '7 hours'),
    ('7', '8 hours'),
    ('8', '9 hours'),
    ('9', '10 hours'),
    ('10', '11 hours'),
    ('11', '12 hours'),
    ('12', '13 hours'),
    ('13', '14 hours'),
    ('14', '15 hours'),
    ('15', '16 hours'),
    ('16', '17 hours'),
    ('17', '18 hours'),
    ('18', '19 hours'),
    ('19', '20 hours'),
    ('20', '21 hours'),
    ('21', '22 hours'),
    ('22', '23 hours'),
    ('23', '24 hours'),
)

pre_processing_select_options = (
    ('0', 'no'),
    ('1', 'yes'),
)
# Create your models here.


class NewProcess(models.Model):
    process_name = models.CharField(max_length=30)
    pipeline = models.CharField(
        max_length=30, choices=pipeline_select_options, null=True, blank=True)
    classification_model = models.CharField(
        max_length=30, choices=classification_model_select_options, null=True, blank=True)
    input_document = MultiSelectField(
        choices=input_document_select_options, null=True, max_choices=5, blank=True)
    time_zone = models.CharField(
        max_length=30, choices=time_zone_select_options, null=True, blank=True)
    process_sla = models.CharField(
        max_length=30, choices=process_sla_select_options, null=True, blank=True)
    pre_processing = models.CharField(
        max_length=30, choices=pre_processing_select_options, null=True, blank=True)
    # username = models.ForeignKey(
    #     User, to_field="username", on_delete=models.CASCADE,null=True)





type_select_option = (
    ('regular model', 'Regular Model'),
    ('vgg16 model', 'Vgg16 Model'),
)

epochs_select_option = (
    ('20','20'),
    ('30','30'),
    ('40','40'),
    ('50','50'),
    ('60','60'),
    ('70','70'),
    ('80','80'),
    ('90','90'),
    ('100','100'),
)

batch_select_option = (
    ('16','16'),
    ('32','32'),
    ('64','64'),
)

kernal_select_option = (
    ('he_normal','he_normal'),
    ('he_uniform','he_uniform'),
)

optimizer_select_option = (
    ('adam','adam'),
    ('sgd','sgd'),
    ('rmsprop','rmsprop'),
)
test_select_option = (
    ('0.3','0.3'),
    ('0.15','0.15'),
    ('0.18','0.18'),
    ('0.21','0.21'),
    ('0.24','0.24'),
    ('0.27','0.27'),
)

activation_select_option = (
    ('relu','relu'),
    ('leaky relu','leaky relu')
)

class AddCnn(models.Model):
    type = models.CharField(max_length=30, choices=type_select_option)
    name = models.CharField(max_length=30,)
    confidence_threshold = models.IntegerField(max_length=30,)
    sample_file = models.FileField()
    epochs = models.CharField(max_length=30, choices=epochs_select_option)
    batch_size = models.CharField(max_length=30, choices=batch_select_option)
    kernal_initializer = models.CharField(max_length=30, choices=kernal_select_option)
    optimizer = models.CharField(max_length=30, choices=optimizer_select_option)
    test_size = models.CharField(max_length=30, choices=test_select_option)
    activation = models.CharField(max_length=30, choices=activation_select_option)
