from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User


class BaseModel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
