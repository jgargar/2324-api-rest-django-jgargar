# Generated by Django 5.0.2 on 2024-02-13 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patinetes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='user',
        ),
    ]
