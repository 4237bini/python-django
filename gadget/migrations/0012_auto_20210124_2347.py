# Generated by Django 3.1.4 on 2021-01-24 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0011_remove_smartphone_image3s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='image1s',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='image2s',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='image3',
        ),
    ]