# Generated by Django 4.2.7 on 2023-12-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_details', '0002_alter_carmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='model_year',
            field=models.IntegerField(),
        ),
    ]
