# Generated by Django 5.1.3 on 2024-12-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0010_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='Year_Of_Admission',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
