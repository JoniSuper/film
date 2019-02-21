from django.db import models

# Create your models here.

from django.db import models

class newsIndex(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}'.format(self.title)
