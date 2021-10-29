# Generated by Django 3.1.4 on 2021-01-22 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, unique=True)),
                ('display', models.CharField(max_length=255, null=True)),
                ('processor', models.CharField(max_length=255, null=True)),
                ('memory', models.CharField(max_length=255, null=True)),
                ('camera', models.CharField(max_length=150, null=True)),
                ('battery', models.CharField(max_length=150, null=True)),
                ('colors', models.CharField(max_length=150, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('image1', models.ImageField(null=True, upload_to='img')),
                ('image2', models.ImageField(null=True, upload_to='img')),
                ('image3', models.ImageField(null=True, upload_to='img')),
                ('averageRatings', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmartphoneDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(blank=True, max_length=250)),
                ('ratings', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gadget.smartphone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
