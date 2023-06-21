# Generated by Django 4.2.2 on 2023-06-21 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_team_google_plus_link_alter_team_twitter_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]