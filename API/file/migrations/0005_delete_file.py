# Generated by Django 4.2.11 on 2024-04-05 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_file_created_at_file_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]