# Generated by Django 4.2.5 on 2024-05-04 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='field_name',
            new_name='photo',
        ),
    ]
