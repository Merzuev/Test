from django.db import models

class Note(models.Model):
    title = models.CharField (max_length=30)
    content = models.TextField (max_length= 500)
    create_at = models.DateTimeField(auto_now_add=True)