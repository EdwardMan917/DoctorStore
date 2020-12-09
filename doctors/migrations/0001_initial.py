# Generated by Django 3.1.3 on 2020-12-09 09:53

from django.db import migrations, models
import django.db.models.deletion
import uuid
from doctors.data import create

def forwards_func(apps, schema_editor):
    create()

def reverse_func(apps, schema_editor):
    return


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('district', models.CharField(db_index=True, max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(db_index=True)),
                ('remarks', models.CharField(max_length=255, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='doctors.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('details', models.CharField(max_length=255)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_hours', to='doctors.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('query_name', models.CharField(db_index=True, default='', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='doctors.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('query_name', models.CharField(db_index=True, default='', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='doctors.doctor')),
            ],
        ),
        migrations.RunPython(forwards_func, reverse_func)
    ]
