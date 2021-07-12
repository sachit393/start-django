# Generated by Django 3.2 on 2021-07-12 03:43

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
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=200, unique=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('college', models.CharField(max_length=50)),
                ('phone_no', models.CharField(default='', max_length=30)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('description', models.TextField(blank=True)),
                ('cv', models.URLField(null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('year', models.IntegerField(null=True)),
                ('degree', models.CharField(max_length=200, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('contact', models.URLField(blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
