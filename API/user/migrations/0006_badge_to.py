# Generated by Django 4.2.11 on 2024-04-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_badge'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='to',
            field=models.ManyToManyField(related_name='badges', to='user.profile'),
        ),
    ]