# Generated by Django 3.2.7 on 2021-09-07 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='updatetd_at',
            new_name='updated_at',
        ),
    ]
