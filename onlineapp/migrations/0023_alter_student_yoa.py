# Generated by Django 5.1.3 on 2024-12-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0022_merge_20241206_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='yoa',
            field=models.IntegerField(),
        ),
    ]
