# Generated by Django 4.2.11 on 2024-04-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
