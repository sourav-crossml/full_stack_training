# Generated by Django 3.1.7 on 2022-06-24 09:35

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cde', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newprocess',
            name='classification_model',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newprocess',
            name='input_document',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('JPG', 'JPG'), ('PDF', 'PDF'), ('JPEG', 'JPEG'), ('TIF', 'TIF'), ('PNG', 'PNG')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newprocess',
            name='pipeline',
            field=models.CharField(blank=True, choices=[('Engine-I', 'Engine-I'), ('Engine-II', 'Engine-II')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newprocess',
            name='pre_processing',
            field=models.CharField(blank=True, choices=[('Dfgdfg', 'no'), ('DFgdfggfd', 'yes')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newprocess',
            name='process_sla',
            field=models.CharField(blank=True, choices=[('afafd', '(UTC-12:00)Universal Coordinated Time GMT'), ('afafsdd', '(EET) Eastern European Time GMT+2:00'), ('afafddf', '(IST) India Standard Time\tGMT+5:30')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='newprocess',
            name='time_zone',
            field=models.CharField(blank=True, choices=[('afafd', '(UTC-12:00)Universal Coordinated Time GMT'), ('afafsdd', '(EET) Eastern European Time GMT+2:00'), ('afafddf', '(IST) India Standard Time\tGMT+5:30')], max_length=30, null=True),
        ),
    ]
