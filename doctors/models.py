from django.db import models
from django.db.models import (
    ForeignKey, 
    UUIDField, 
    CharField, 
    PositiveIntegerField,
    OneToOneField
)

import uuid

class Doctor(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(null=False, max_length=255)
    address = CharField(null=False, max_length=255)
    district = CharField(null=False, max_length=255, db_index=True)
    phone_number = CharField(null=False, max_length=20)


class Category(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = ForeignKey("Doctor", on_delete=models.CASCADE, related_name="categories")
    query_name = CharField(null=False, default='', max_length=255, db_index=True)
    name = CharField(null=False, max_length=255)


class Language(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = ForeignKey("Doctor", on_delete=models.CASCADE, related_name="languages")
    query_name = CharField(null=False, default='', max_length=255, db_index=True)
    name = CharField(null=False, max_length=255)


class Service(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = ForeignKey("Doctor", on_delete=models.CASCADE, related_name="services")
    category = OneToOneField("Category", on_delete=models.DO_NOTHING, related_name="category")
    item = CharField(null=False, max_length=255)
    price = PositiveIntegerField(null=False, db_index=True)
    remarks = CharField(null=True, max_length=255)


class OpeningHours(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = ForeignKey("Doctor", on_delete=models.CASCADE, related_name="opening_hours")
    details = CharField(null=False, max_length=255)