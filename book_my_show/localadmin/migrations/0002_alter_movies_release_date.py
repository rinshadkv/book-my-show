# Generated by Django 4.0.1 on 2022-09-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Release_date',
            field=models.DateField(),
        ),
    ]
