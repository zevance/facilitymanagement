# Generated by Django 5.0.6 on 2024-05-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='facility_name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
