# Generated by Django 3.1.4 on 2021-01-25 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gadget', '0013_smartwatch_smartwatchdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='image1s',
            field=models.ImageField(null=True, upload_to='img/smartphone/'),
        ),
        migrations.AlterField(
            model_name='smartwatchdetail',
            name='smartwatch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gadget.smartwatch'),
        ),
    ]
