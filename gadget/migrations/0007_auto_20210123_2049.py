# Generated by Django 3.1.4 on 2021-01-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0006_auto_20210123_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='price',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
