# Generated by Django 4.1.1 on 2022-09-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_name', models.CharField(max_length=100)),
                ('Release_date', models.CharField(max_length=20)),
                ('Movie_poster', models.ImageField(upload_to='media/poster')),
                ('Languages', models.CharField(max_length=120)),
                ('Gener', models.CharField(max_length=1000)),
                ('About_movie', models.CharField(max_length=20000)),
                ('Movie_trailor', models.FileField(upload_to='media/trailor')),
                ('Movie_duaration', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'movie_tb',
            },
        ),
    ]
