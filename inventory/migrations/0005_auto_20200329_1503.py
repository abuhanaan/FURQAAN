# Generated by Django 3.0.2 on 2020-03-29 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20200328_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='cashier',
            new_name='user',
        ),
    ]
