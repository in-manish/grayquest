from django.db import models
from django.contrib.sessions.models import Session


class Cookie(models.Model):
    session = models.ForeignKey(Session, related_name='session_cookies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
