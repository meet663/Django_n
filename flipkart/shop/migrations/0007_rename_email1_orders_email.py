# Generated by Django 5.0.3 on 2024-04-19 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_email_orders_email1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='email1',
            new_name='email',
        ),
    ]
