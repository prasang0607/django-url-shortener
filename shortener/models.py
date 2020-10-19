from django.db import models


class URL(models.Model):
    full_url = models.URLField(unique=True, null=True)
    file_path = models.FileField(null=True, upload_to='uploads')
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url_hash
