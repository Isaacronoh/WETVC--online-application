# Generated by Django 5.1.3 on 2024-12-06 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0018_remove_student_user_id_alter_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id_number',
        ),
    ]
