# Generated by Django 5.1.3 on 2024-12-02 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0011_application_year_of_admission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='Year_Of_Admission',
            new_name='year_of_admission',
        ),
    ]
