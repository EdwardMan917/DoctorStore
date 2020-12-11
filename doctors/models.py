from django.db import models
from django.db.models import (
    ForeignKey, 
    UUIDField, 
    TextField, 
    SlugField,
    PositiveIntegerField
)
import uuid

class Doctor(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = TextField()
    address = TextField()
    district = SlugField(max_length=100)
    phone_number = TextField(max_length=50)


class Category(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = ForeignKey("Doctor", on_delete=models.PROTECT, related_name="categories")
    query_name = SlugField()
    display_name = TextField()


class Language(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = ForeignKey("Doctor", on_delete=models.PROTECT, related_name="languages")
    query_name = SlugField()
    display_name = TextField()


class Service(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    category = ForeignKey("Category", on_delete=models.PROTECT, related_name="services")
    item = TextField()
    price = PositiveIntegerField(db_index=True)
    remarks = TextField(null=True)


class OpeningHour(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = ForeignKey("Doctor", on_delete=models.PROTECT, related_name="opening_hours")
    details = TextField()
