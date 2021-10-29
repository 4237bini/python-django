# Generated by Django 3.1.4 on 2021-01-25 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gadget', '0012_auto_20210124_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartwatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, unique=True)),
                ('design', models.CharField(max_length=255, null=True)),
                ('display', models.CharField(max_length=255, null=True)),
                ('activityTracker', models.CharField(max_length=255, null=True)),
                ('sensor', models.CharField(max_length=255, null=True)),
                ('memory', models.CharField(max_length=150, null=True)),
                ('battery', models.CharField(max_length=150, null=True)),
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
            name='SmartwatchDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10)),
                ('review', models.CharField(blank=True, max_length=250)),
                ('ratings', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('smartwatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gadget.smartphone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
