# Generated by Django 5.0 on 2023-12-17 16:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentDetails',
            fields=[
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('show_flag', models.BooleanField(default=True)),
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=500)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryDetails',
            fields=[
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('show_flag', models.BooleanField(default=True)),
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=500)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deparment_store.departmentdetails')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationDetails',
            fields=[
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('show_flag', models.BooleanField(default=True)),
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=500)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='departmentdetails',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deparment_store.locationdetails'),
        ),
        migrations.CreateModel(
            name='SubCategoryDetails',
            fields=[
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('show_flag', models.BooleanField(default=True)),
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=500)),
                ('categoryt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deparment_store.categorydetails')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]