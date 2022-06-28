from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


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
    ('UTC-12:00, International Date Line West',
     '(UTC-12:00) International Date Line West'),
    ('UTC-11:00, Coordinated Universal Time-11',
     '(UTC-11:00) Coordinated Universal Time-11'),
    ('UTC-10:00, Aleutian Islands', '(UTC-10:00) Aleutian Islands'),
    ('UTC-10:00, Hawaii', '(UTC-10:00) Hawaii'),
    ('UTC-09:30, Marquesas Islands', '(UTC-09:30) Marquesas Islands'),
    ('UTC-09:00, Alaska', '(UTC-09:00) Alaska'),
    ('UTC-09:00, Coordinated Universal Time-09',
     '(UTC-09:00) Coordinated Universal Time-09'),
    ('UTC-08:00, Baja California', '(UTC-08:00) Baja California'),
    ('UTC-08:00, Coordinated Universal Time-08',
     '(UTC-08:00) Coordinated Universal Time-08'),
    ('UTC-08:00, Pacific Time (US & Canada)',
     '(UTC-08:00) Pacific Time (US & Canada)'),
    ('UTC-07:00, Arizona', '(UTC-07:00) Arizona'),
    ('UTC-07:00, Chihuahua, La Paz, Mazatlan',
     '(UTC-07:00) Chihuahua, La Paz, Mazatlan'),
    ('UTC-07:00, Mountain Time (US & Canada)',
     '(UTC-07:00) Mountain Time (US & Canada)'),
    ('UTC-06:00, Central America', '(UTC-06:00) Central America'),
    ('UTC-06:00, Central Time (US & Canada)',
     '(UTC-06:00) Central Time (US & Canada)'),
    ('UTC-06:00, Easter Island', '(UTC-06:00) Easter Island'),
    ('UTC-06:00, Guadalajara, Mexico City, Monterrey',
     '(UTC-06:00) Guadalajara, Mexico City, Monterrey'),
    ('UTC-06:00, Saskatchewan', '(UTC-06:00) Saskatchewan'),
    ('UTC-05:00, Bogota, Lima, Quito, Rio Branco',
     '(UTC-05:00) Bogota, Lima, Quito, Rio Branco'),
    ('UTC-05:00, Chetumal', '(UTC-05:00) Chetumal'),
    ('UTC-05:00, Eastern Time (US & Canada)',
     '(UTC-05:00) Eastern Time (US & Canada)'),
    ('UTC-05:00, Haiti', '(UTC-05:00) Haiti'),
    ('UTC-05:00, Havana', '(UTC-05:00) Havana'),
    ('UTC-05:00, Indiana (East)', '(UTC-05:00) Indiana (East)'),
    ('UTC-05:00, Turks and Caicos', '(UTC-05:00) Turks and Caicos'),
    ('UTC-04:00, Asuncion', '(UTC-04:00) Asuncion'),
    ('UTC-04:00, Atlantic Time (Canada)', '(UTC-04:00) Atlantic Time (Canada)'),
    ('UTC-04:00, Caracas', '(UTC-04:00) Caracas'),
    ('UTC-04:00, Cuiaba', '(UTC-04:00) Cuiaba'),
    ('UTC-04:00, Georgetown, La Paz, Manaus, San Juan',
     '(UTC-04:00) Georgetown, La Paz, Manaus, San Juan'),
    ('UTC-04:00, Santiago', '(UTC-04:00) Santiago'),
    ('UTC-03:30, Newfoundland', '(UTC-03:30) Newfoundland'),
    ('UTC-03:00, Araguaina', '(UTC-03:00) Araguaina'),
    ('UTC-03:00, Brasilia', '(UTC-03:00) Brasilia'),
    ('UTC-03:00, Cayenne, Fortaleza', '(UTC-03:00) Cayenne, Fortaleza'),
    ('UTC-03:00, City of Buenos Aires', '(UTC-03:00) City of Buenos Aires'),
    ('UTC-03:00, Greenland', '(UTC-03:00) Greenland'),
    ('UTC-03:00, Montevideo', '(UTC-03:00) Montevideo'),
    ('UTC-03:00, Punta Arenas', '(UTC-03:00) Punta Arenas'),
    ('UTC-03:00, Saint Pierre and Miquelon',
     '(UTC-03:00) Saint Pierre and Miquelon'),
    ('UTC-03:00, Salvador', '(UTC-03:00) Salvador'),
    ('UTC-02:00, Coordinated Universal Time-02',
     '(UTC-02:00) Coordinated Universal Time-02'),
    ('UTC-01:00, Azores', '(UTC-01:00) Azores'),
    ('UTC-01:00, ', '(UTC-01:00) Cabo Verde Is.'),
    ('UTC, Coordinated Universal Time', '(UTC) Coordinated Universal Time'),
    ('UTC+00:00, Dublin, Edinburgh, Lisbon, London',
     '(UTC+00:00) Dublin, Edinburgh, Lisbon, London'),
    ('UTC+00:00, Monrovia, Reykjavik', '(UTC+00:00) Monrovia, Reykjavik'),
    ('UTC+00:00, Sao Tome', '(UTC+00:00) Sao Tome'),
    ('UTC+01:00, Casablanca', '(UTC+01:00) Casablanca'),
    ('UTC+01:00, Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna',
     '(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna'),
    ('UTC+01:00, Belgrade, Bratislava, Budapest, Ljubljana, Prague',
     '(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague'),
    ('UTC+01:00, Brussels, Copenhagen, Madrid, Paris',
     '(UTC+01:00) Brussels, Copenhagen, Madrid, Paris'),
    ('UTC+01:00, Sarajevo, Skopje, Warsaw, Zagreb',
     '(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb'),
    ('UTC+01:00, West Central Africa', '(UTC+01:00) West Central Africa'),
    ('UTC+02:00, Amman', '(UTC+02:00) Amman'),
    ('UTC+02:00, Athens, Bucharest', '(UTC+02:00) Athens, Bucharest'),
    ('UTC+02:00, Beirut', '(UTC+02:00) Beirut'),
    ('UTC+02:00, Cairo', '(UTC+02:00) Cairo'),
    ('UTC+02:00, Chisinau', '(UTC+02:00) Chisinau'),
    ('UTC+02:00, Damascus', '(UTC+02:00) Damascus'),
    ('UTC+02:00, Gaza, Hebron', '(UTC+02:00) Gaza, Hebron'),
    ('UTC+02:00, Harare, Pretoria', '(UTC+02:00) Harare, Pretoria'),
    ('UTC+02:00, Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius',
     '(UTC+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius'),
    ('UTC+02:00, Jerusalem', '(UTC+02:00) Jerusalem'),
    ('UTC+02:00, Kaliningrad', '(UTC+02:00) Kaliningrad'),
    ('UTC+02:00, Khartoum', '(UTC+02:00) Khartoum'),
    ('UTC+02:00, Tripoli', '(UTC+02:00) Tripoli'),
    ('UTC+02:00, Windhoek', '(UTC+02:00) Windhoek'),
    ('UTC+03:00, Baghdad', '(UTC+03:00) Baghdad'),
    ('UTC+03:00, Istanbul', '(UTC+03:00) Istanbul'),
    ('UTC+03:00, Kuwait, Riyadh', '(UTC+03:00) Kuwait, Riyadh'),
    ('UTC+03:00, Minsk', '(UTC+03:00) Minsk'),
    ('UTC+03:00, Moscow, St. Petersburg', '(UTC+03:00) Moscow, St. Petersburg'),
    ('UTC+03:00, Nairobi', '(UTC+03:00) Nairobi'),
    ('UTC+03:30, Tehran', '(UTC+03:30) Tehran'),
    ('UTC+04:00, Abu Dhabi, Muscat', '(UTC+04:00) Abu Dhabi, Muscat'),
    ('UTC+04:00, Astrakhan, Ulyanovsk', '(UTC+04:00) Astrakhan, Ulyanovsk'),
    ('UTC+04:00, Baku', '(UTC+04:00) Baku'),
    ('UTC+04:00, Izhevsk, Samara', '(UTC+04:00) Izhevsk, Samara'),
    ('UTC+04:00, Port Louis', '(UTC+04:00) Port Louis'),
    ('UTC+04:00, Saratov', '(UTC+04:00) Saratov'),
    ('UTC+04:00, Tbilisi', '(UTC+04:00) Tbilisi'),
    ('UTC+04:00, Volgograd', '(UTC+04:00) Volgograd'),
    ('UTC+04:00, Yerevan', '(UTC+04:00) Yerevan'),
    ('UTC+04:30, Kabul', '(UTC+04:30) Kabul'),
    ('UTC+05:00, Ashgabat, Tashkent', '(UTC+05:00) Ashgabat, Tashkent'),
    ('UTC+05:00, Ekaterinburg', '(UTC+05:00) Ekaterinburg'),
    ('UTC+05:00, Islamabad, Karachi', '(UTC+05:00) Islamabad, Karachi'),
    ('UTC+05:00, Qyzylorda', '(UTC+05:00) Qyzylorda'),
    ('UTC+05:30, Chennai, Kolkata, Mumbai, New Delhi',
     '(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi'),
    ('UTC+05:30, Sri Jayawardenepura', '(UTC+05:30) Sri Jayawardenepura'),
    ('UTC+05:45, Kathmandu', '(UTC+05:45) Kathmandu'),
    ('UTC+06:00, Astana', '(UTC+06:00) Astana'),
    ('UTC+06:00, Dhaka', '(UTC+06:00) Dhaka'),
    ('UTC+06:00, Omsk', '(UTC+06:00) Omsk'),
    ('UTC+06:30, Yangon (Rangoon)', '(UTC+06:30) Yangon (Rangoon)'),
    ('UTC+07:00, Bangkok, Hanoi, Jakarta', '(UTC+07:00) Bangkok, Hanoi, Jakarta'),
    ('UTC+07:00, Barnaul, Gorno-Altaysk', '(UTC+07:00) Barnaul, Gorno-Altaysk'),
    ('UTC+07:00, Hovd', '(UTC+07:00) Hovd'),
    ('UTC+07:00, Krasnoyarsk', '(UTC+07:00) Krasnoyarsk'),
    ('UTC+07:00, Novosibirsk', '(UTC+07:00) Novosibirsk'),
    ('UTC+07:00, Tomsk', '(UTC+07:00) Tomsk'),
    ('UTC+08:00, Beijing, Chongqing, Hong Kong, Urumqi',
     '(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi'),
    ('UTC+08:00, Irkutsk', '(UTC+08:00) Irkutsk'),
    ('UTC+08:00, Kuala Lumpur, Singapore', '(UTC+08:00) Kuala Lumpur, Singapore'),
    ('UTC+08:00, Perth', '(UTC+08:00) Perth'),
    ('UTC+08:00, Taipei', '(UTC+08:00) Taipei'),
    ('UTC+08:00, Ulaanbaatar', '(UTC+08:00) Ulaanbaatar'),
    ('UTC+08:45, Eucla', '(UTC+08:45) Eucla'),
    ('UTC+09:00, Chita', '(UTC+09:00) Chita'),
    ('UTC+09:00, Osaka, Sapporo, Tokyo', '(UTC+09:00) Osaka, Sapporo, Tokyo'),
    ('UTC+09:00, Pyongyang', '(UTC+09:00) Pyongyang'),
    ('UTC+09:00, Seoul', '(UTC+09:00) Seoul'),
    ('UTC+09:00, Yakutsk', '(UTC+09:00) Yakutsk'),
    ('UTC+09:30, Adelaide', '(UTC+09:30) Adelaide'),
    ('UTC+09:30, Darwin', '(UTC+09:30) Darwin'),
    ('UTC+10:00, Brisbane', '(UTC+10:00) Brisbane'),
    ('UTC+10:00, Canberra, Melbourne, Sydney',
     '(UTC+10:00) Canberra, Melbourne, Sydney'),
    ('UTC+10:00, Guam, Port Moresby', '(UTC+10:00) Guam, Port Moresby'),
    ('UTC+10:00, Hobart', '(UTC+10:00) Hobart'),
    ('UTC+10:00, Vladivostok', '(UTC+10:00) Vladivostok'),
    ('UTC+10:30, Lord Howe Island', '(UTC+10:30) Lord Howe Island'),
    ('UTC+11:00, Bougainville Island', '(UTC+11:00) Bougainville Island'),
    ('UTC+11:00, Chokurdakh', '(UTC+11:00) Chokurdakh'),
    ('UTC+11:00, Magadan', '(UTC+11:00) Magadan'),
    ('UTC+11:00, Norfolk Island', '(UTC+11:00) Norfolk Island'),
    ('UTC+11:00, Sakhalin', '(UTC+11:00) Sakhalin'),
    ('UTC+11:00, Solomon Is., New Caledonia',
     '(UTC+11:00) Solomon Is., New Caledonia'),
    ('UTC+12:00, Anadyr, Petropavlovsk-Kamchatsky',
     '(UTC+12:00) Anadyr, Petropavlovsk-Kamchatsky'),
    ('UTC+12:00, Auckland, Wellington', '(UTC+12:00) Auckland, Wellington'),
    ('UTC+12:00, Coordinated Universal Time+12',
     '(UTC+12:00) Coordinated Universal Time+12'),
    ('UTC+12:00, Fiji', '(UTC+12:00) Fiji'),
    ('UTC+12:45, Chatham Islands', '(UTC+12:45) Chatham Islands'),
    ('UTC+13:00, Coordinated Universal Time+13',
     '(UTC+13:00) Coordinated Universal Time+13'),
    ('UTC+13:00, Nuku’alofa', '(UTC+13:00) Nuku’alofa'),
    ('UTC+13:00, Samoa', '(UTC+13:00) Samoa'),
    ('UTC+14:00, Kiritimati Island', '(UTC+14:00) Kiritimati Island'),
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
    process_name = models.CharField(max_length=60)
    pipeline = models.CharField(
        max_length=30, choices=pipeline_select_options, null=True, blank=True)
    classification_model = models.CharField(
        max_length=30, choices=classification_model_select_options, null=True, blank=True)
    input_document = MultiSelectField(
        choices=input_document_select_options, null=True, max_choices=5, blank=True)
    time_zone = models.CharField(
        max_length=60, choices=time_zone_select_options, null=True, blank=True)
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
    ('20', '20'),
    ('30', '30'),
    ('40', '40'),
    ('50', '50'),
    ('60', '60'),
    ('70', '70'),
    ('80', '80'),
    ('90', '90'),
    ('100', '100'),
)

batch_select_option = (
    ('16', '16'),
    ('32', '32'),
    ('64', '64'),
)

kernal_select_option = (
    ('he_normal', 'he_normal'),
    ('he_uniform', 'he_uniform'),
)

optimizer_select_option = (
    ('adam', 'adam'),
    ('sgd', 'sgd'),
    ('rmsprop', 'rmsprop'),
)
test_select_option = (
    ('0.3', '0.3'),
    ('0.15', '0.15'),
    ('0.18', '0.18'),
    ('0.21', '0.21'),
    ('0.24', '0.24'),
    ('0.27', '0.27'),
)

activation_select_option = (
    ('relu', 'relu'),
    ('leaky relu', 'leaky relu')
)


class AddCnn(models.Model):
    type = models.CharField(max_length=30, choices=type_select_option)
    name = models.CharField(max_length=30,)
    confidence_threshold = models.IntegerField(max_length=30,)
    sample_file = models.FileField(
        upload_to="media/", blank=True, validators=[FileExtensionValidator(['.zip', ])])
    epochs = models.CharField(max_length=30, choices=epochs_select_option)
    batch_size = models.CharField(max_length=30, choices=batch_select_option)
    kernal_initializer = models.CharField(
        max_length=30, choices=kernal_select_option)
    optimizer = models.CharField(
        max_length=30, choices=optimizer_select_option)
    test_size = models.CharField(max_length=30, choices=test_select_option)
    activation = models.CharField(
        max_length=30, choices=activation_select_option)


attribute_type_select_option = (
    ('key_item', 'key_item'),
    ('line_item', 'line_item'),
)
is_derived_select_option = (
    ('no', 'no'),
    ('yes', 'yes'),
)
zone_select_option = (
    ('unknown', 'Unknown'),
    ('top', 'top'),
    ('top_right', 'top_right'),
    ('center', 'center'),
    ('bootom_left', 'bootom_left'),
    ('bootom_right', 'bootom_right'),
    ('bootom', 'bootom'),
    ('page', 'page'),
)

required_in_qc_select_option = (
    ('no', 'no'),
    ('yes', 'yes'),
)
required_in_output_select_option = (
    ('no', 'no'),
    ('yes', 'yes'),
)
mandate_select_option = (
    ('no', 'no'),
    ('yes', 'yes'),
)
value_type_select_option = (
    ('string', 'string'),
)


class ManageAttribute(models.Model):
    attribute_name = models.CharField(max_length=30)
    attribute_type = models.CharField(
        max_length=30, choices=attribute_type_select_option)
    attribute_cs = models.CharField(max_length=30)
    is_derived = models.CharField(
        max_length=30, choices=is_derived_select_option)
    min_lenght = models.IntegerField()
    max_lenght = models.IntegerField()
    Zone = models.CharField(max_length=30, choices=zone_select_option)
    default_value = models.CharField(max_length=30)
    required_in_qc = models.CharField(
        max_length=30, choices=required_in_qc_select_option)
    required_in_output = models.CharField(
        max_length=30, choices=required_in_output_select_option)
    mandate = models.CharField(
        max_length=30, choices=mandate_select_option)
    data_label = models.FileField(upload_to='media/data_label')
    value_type = models.CharField(
        max_length=30, choices=value_type_select_option)