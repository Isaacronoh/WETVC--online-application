# Generated by Django 5.1.3 on 2024-12-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0017_student_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=250),
        ),
    ]