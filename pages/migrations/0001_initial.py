# Generated by Django 4.2.1 on 2023-05-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('twitter_link', models.URLField(max_length=100)),
                ('google_plus_link', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
