# Generated by Django 3.1.4 on 2021-01-23 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0010_smartphonedetail_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='image3s',
        ),
    ]
