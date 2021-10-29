# Generated by Django 3.1.4 on 2021-02-04 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gadget', '0014_auto_20210125_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, unique=True)),
                ('display', models.CharField(max_length=255, null=True)),
                ('processor', models.CharField(max_length=255, null=True)),
                ('os', models.CharField(max_length=255, null=True)),
                ('memory', models.CharField(max_length=150, null=True)),
                ('graphics', models.CharField(max_length=150, null=True)),
                ('storage', models.CharField(max_length=255, null=True)),
                ('batteryLife', models.CharField(max_length=150, null=True)),
                ('price', models.CharField(max_length=150, null=True)),
                ('image', models.ImageField(null=True, upload_to='img/smartwatch/')),
                ('image1', models.ImageField(null=True, upload_to='img/smartwatch/')),
                ('image1s', models.ImageField(null=True, upload_to='img/smartwatch/')),
                ('averageRatings', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LaptopDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10)),
                ('review', models.CharField(blank=True, max_length=250)),
                ('ratings', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gadget.laptop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]