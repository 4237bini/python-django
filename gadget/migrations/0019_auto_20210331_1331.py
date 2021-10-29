# Generated by Django 3.1.4 on 2021-03-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0018_laptopdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartwatch',
            name='id',
        ),
        migrations.AddField(
            model_name='smartwatch',
            name='smartwatch_id',
            field=models.PositiveIntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
