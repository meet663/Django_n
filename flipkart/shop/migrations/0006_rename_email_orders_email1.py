# Generated by Django 5.0.3 on 2024-04-19 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='email',
            new_name='email1',
        ),
    ]
