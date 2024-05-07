# Generated by Django 4.2.5 on 2024-05-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='type',
            new_name='event_type',
        ),
        migrations.AlterField(
            model_name='event',
            name='available_seats',
            field=models.IntegerField(editable=False, verbose_name='Доступное количество мест'),
        ),
    ]
