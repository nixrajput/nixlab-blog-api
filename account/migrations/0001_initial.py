# Generated by Django 3.2.5 on 2021-07-20 20:41

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(blank=True, max_length=20, null=True, verbose_name='Gender')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('about', models.CharField(blank=True, max_length=150, null=True, verbose_name='About')),
                ('account_type', models.CharField(blank=True, default='public', max_length=10, verbose_name='Account Type')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Login')),
                ('is_valid', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is Admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is Superuser')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('timestamp', models.CharField(blank=True, max_length=100, null=True, verbose_name='Timestamp')),
                ('followers', models.ManyToManyField(blank=True, related_name='account_followers', to=settings.AUTH_USER_MODEL, verbose_name='Followers')),
                ('following', models.ManyToManyField(blank=True, related_name='account_following', to=settings.AUTH_USER_MODEL, verbose_name='Following')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'All Users',
            },
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=account.models.image_path, verbose_name='Picture')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Upload Time')),
                ('timestamp', models.CharField(blank=True, max_length=100, null=True, verbose_name='Timestamp')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Profile Picture',
                'verbose_name_plural': 'Profile Pictures',
            },
        ),
    ]
