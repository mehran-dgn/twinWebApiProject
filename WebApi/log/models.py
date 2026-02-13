from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ActivityLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    action = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    message = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.created_at}"


