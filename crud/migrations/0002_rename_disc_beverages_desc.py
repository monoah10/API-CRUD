# Generated by Django 4.1.1 on 2022-09-14 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beverages',
            old_name='disc',
            new_name='desc',
        ),
    ]
