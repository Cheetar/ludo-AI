from django.db import models
from django.conf import settings
# Create your models here.
class Code(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20000)

    def __str__(self):
        return self.title
